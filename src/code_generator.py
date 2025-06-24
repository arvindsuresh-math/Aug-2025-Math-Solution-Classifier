# REFACTOR: Standard imports + asyncio and nest_asyncio for Jupyter compatibility.
import pandas as pd
import numpy as np
import time
import datetime
import importlib
import inspect
import os
import re
import json
import random
import openai
import google.generativeai as genai
import anthropic
import asyncio
import nest_asyncio
from openai import AsyncOpenAI # REFACTOR: Import async client
from anthropic import AsyncClient # REFACTOR: Import async client
from datasets import load_dataset
from tqdm.notebook import tqdm # REFACTOR: Use notebook-friendly tqdm
from dotenv import load_dotenv
from typing import List, Dict, Any
from pathlib import Path
import textwrap, hashlib

def find_project_root():
    """Traverse upwards to find the project root, marked by the .git folder."""
    current_path = Path.cwd()
    while current_path != current_path.parent:
        if (current_path / ".git").is_dir():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError("Could not find project root. Is this a git repository?")

# REFACTOR: Apply nest_asyncio to allow asyncio to run in a Jupyter notebook.
# This must be done once per kernel.
nest_asyncio.apply()

# --- 1. Client and Model Configuration ---

load_dotenv()

# REFACTOR: Initialize asynchronous clients.
# The synchronous clients are no longer needed for the generation script.
openai_client_async = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client_async = AsyncClient(api_key=os.getenv("ANTHROPIC_API_KEY"))
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the project root as a global constant
PROJECT_ROOT = find_project_root()
print(f"Project root identified: {PROJECT_ROOT}")
BASE_OUTPUT_DIR = PROJECT_ROOT / 'data' / 'code_gen_outputs_raw'

# A safe starting point is slightly below the documented RPM.
API_CONCURRENCY_LIMITS = {
    "google":    2,   # 2 parallel calls ≈ 30 RPM  < 10 RPM × 3 models
    "anthropic": 2,   # 2 × 3 500 tokens × 60/4 ≈ 105 k TPM → still too high
    "openai":    4,   # unchanged
}

# --- 2. System Prompt and Helper Functions (no changes needed) ---

SYSTEM_PROMPT = "You are an expert Python programmer specializing in data formalization. Your role is to meticulously convert natural language math problems and their step-by-step solutions into a single, well-structured Python function. You will be presented with examples of the required format followed by a final task to complete."


PROMPT_GUIDELINES = """### Guidelines

0. **Output wrapping**
   Return the code inside a single ```python … ``` block, and nothing else.

1.  **Function Naming & Docstring:** The function must be named `solve`. It must begin with a docstring that has exactly two lines:
    *   The first line must be: "Index: [Index]." using the index from the task header.
    *   The second line must be a succinct, one-sentence description of what the function returns (e.g., "Returns: the total cost of wages and taxes.").

2.  **Function Arguments:** The function arguments must be derived from the 'Question' text. 
    *   Create a distinct argument for every numerical value that is directly stated in the text.
    *   The arguments should be created **in the same order in which they appear in the question**.
    *   **Note:** Some of these arguments may end up not being used in the function body. This is expected. Do not worry about this and leave the unused arguments in the function signature.

3.  **Argument Formatting:** Each argument must include a type-hint (e.g., `int`, `float`) and a default value equal to its value in the 'Question'. You must also add a comment (`#`) next to each argument that quotes or refers to the phrase in the 'Question' it comes from. 

4.  **Function Body:** The body of the function should follow the logic of the provided 'Solution' dict, which contains the step-by-step solution to the problem. The keys of this dict are strings (e.g. `"L1"`, `"L2"`) which refer to the line number, and the values of the dict are the corresponding steps in the solution. 
    * For every relevant line in the 'Solution', you must include a comment in the Python code that indicates the line number (key) from the 'Solution' dict.
    * These comments should be formatted as `#: L<n>`, where `<n>` is the line number from the 'Solution' dict.
    * Immediately follow the comment with the Python statement that performs the calculation.
    * Steps in the solution should result in the creation of new, intermediate variables, which should be named descriptively based on the context of the calculation.
    * Wherever possible, in your code try to use only the variables from the function arguments and the intermediate variables you created before, and try to avoid using hard-coded numbers in the calculations.

5.  **Calculator Annotations:** Pay close attention to the calculator annotations (e.g., `[[25*8=200]]`) in the 'Solution' as they reveal the precise mathematical operations to implement. **Note**: Some lines in the solution may not contain calculator annotations, but you should still pay attention to the logic and calculations described in those lines.

6.  **Final Answer:** Store the final answer in a variable named 'answer', and on the same line, add the comment `# FINAL ANSWER`. In the next line, return the 'answer' variable.

7. **No extra output:** Your output should end with the ``` closing the code block. Do not include any additional text, explanations, or comments outside of the code block."""

gsm8k_train = load_dataset("gsm8k", "main", split="train")

def build_solution_mapping(
    index: int,
    dataset: Any,
    convert_brackets: bool = True,
):
    """
    Parameters
    ----------
    index : int
        Position of the sample in the loaded dataset.
    dataset : iterable / HuggingFace Dataset
    convert_brackets : bool, default ``True``
        If ``True`` replace every ``<< … >>`` calculator annotation with
        the canonical ``[[ … ]]`` form so downstream code sees a single
        bracket style.

    Returns
    -------
    Dict[str, str]
        Mapping ``{"L1": <first non-empty line>, "L2": <second>, …}``.

    Notes
    -----
    * Blank lines in ``sample["answer"]`` are ignored.
    * The line numbering reflects the *order* in the original solution
      string; there is no semantic grouping beyond that.
    """
    # extract & split solution text
    solution_text = dataset[index]["answer"]
    lines = [ln.strip() for ln in solution_text.splitlines() if ln.strip()]

    # Remove the last line if it matches the '####' answer pattern
    if lines and re.match(r"^####\s*\d+(\.\d+)?$", lines[-1]):
        lines = lines[:-1]

    # optional bracket normalisation
    if convert_brackets:
        angle = re.compile(r"<<([^>]+)>>")
        lines = [angle.sub(r"[[\1]]", ln) for ln in lines]
    # build mapping
    return {f"L{i}": line for i, line in enumerate(lines, 1)}


def format_prompt_query(index: int, code_strings: dict, with_code: bool = False):
    sample = gsm8k_train[index]
    question = sample["question"]
    solution_mapping = build_solution_mapping(index, gsm8k_train)
    solution = json.dumps(solution_mapping)
    out = f"""*Index*: 
{index}

*Question*: 
{question}

*Solution*: 
{solution}

*Code*:"""
    if with_code:
        out += f"""\n```python
{code_strings.get(index, "# Code not found")}
```"""
    return out


def get_code_strings(indices: List[int], savepath: Path = PROJECT_ROOT / 'data' / 'code_examples'):
    """
    Reads code examples directly from .py files instead of importing them.
    This is more robust and avoids Python's complex import path mechanics.
    """
    code_strings = {}
    for idx in indices:
        # Construct the full file path
        filepath = os.path.join(savepath, f"_{idx}.py")
        try:
            # Read the entire content of the file
            with open(filepath, 'r', encoding='utf-8') as f:
                code_strings[idx] = f.read()
        except FileNotFoundError:
            print(f"Error: Could not find example file for index {idx} at: {filepath}")
            code_strings[idx] = f"# Error: Code for example {idx} not found."
    return code_strings


EXAMPLE_INDICES = [310, 3822, 7371]          # keep fixed order
_CODE_EXAMPLES  = get_code_strings(EXAMPLE_INDICES)


def build_static_prefix() -> str:
    """Guidelines + few-shot examples rendered once for caching."""
    examples_block = "\n".join(
        format_prompt_query(idx, _CODE_EXAMPLES, with_code=True)
        for idx in EXAMPLE_INDICES
    )
    prefix = "\n".join([
        PROMPT_GUIDELINES.strip(),
        "\n--- EXAMPLES ---\n",
        examples_block.strip()
    ])
    # Canonical whitespace – important for cache hits
    return textwrap.dedent(prefix).strip()


STATIC_PREFIX = build_static_prefix()
print(STATIC_PREFIX)
print("Static prefix SHA-1:", hashlib.sha1(STATIC_PREFIX.encode()).hexdigest())


def build_task_prompt(index: int) -> str:
    """Problem-specific part that changes every call."""
    return "\n".join([
        "--- TASK ---\n",
        format_prompt_query(index=index,
                            code_strings={},     # no code in the task part
                            with_code=False)
    ])


# --- 3. Asynchronous API Calling Function ---

# ── Anthropic token-bucket limiter ────────────────────────────────────
import time, asyncio, math

# one global bucket: 50 000 input-tokens per rolling minute
_anthropic_bucket = {"tokens": 50_000, "reset_at": time.monotonic() + 60}

async def _anthropic_throttle(tokens_needed: int):
    """
    Wait until at least `tokens_needed` tokens are available in the
    50 000-tokens-per-minute bucket, then deduct them.
    """
    global _anthropic_bucket

    while True:
        now = time.monotonic()

        # reset bucket if a minute passed
        if now >= _anthropic_bucket["reset_at"]:
            _anthropic_bucket = {"tokens": 50_000, "reset_at": now + 60}

        if tokens_needed <= _anthropic_bucket["tokens"]:
            _anthropic_bucket["tokens"] -= tokens_needed
            return                               # we’re clear to send
        else:
            # need to wait for bucket refill
            to_sleep = _anthropic_bucket["reset_at"] - now
            await asyncio.sleep(max(to_sleep, 0.01))


async def _with_429_retries(send_coroutine_factory, *, max_attempts=3, default_wait=15):
    """
    send_coroutine_factory : lambda  ->  coroutine
        Pass a **lambda** that, when called, returns the coroutine you want
        to execute (e.g. the gemini.generate_content_async call).

    Retries up to `max_attempts` times on 429 errors, using the
    `retry_delay` from the API error when available, otherwise `default_wait`.
    """
    attempt = 0
    wait = default_wait
    while True:
        try:
            return await send_coroutine_factory()
        except Exception as e:
            # crude but effective 429 detection
            if ("429" in str(e)) and attempt < max_attempts:
                # Google errors include retry_delay.seconds
                retry_attr = getattr(e, "retry_delay", None)
                wait = retry_attr.seconds if retry_attr else wait
                attempt += 1
                print(f"🕒 Google 429 — retrying in {wait}s (attempt {attempt}/{max_attempts})")
                await asyncio.sleep(wait)
            else:
                raise  # re-raise non-429 or maxed-out errors


async def call_model_api_async(
        provider: str,
        model: str,
        static_prefix: str,
        task_prompt: str,
        semaphore: asyncio.Semaphore):

    async with semaphore:
        usage = {"input_tokens": 0,
                 "output_tokens": 0,
                 "cached_tokens": 0}

        # ─────────────────── Google (no prompt cache) ───────────────────
        if provider == "google":
            gemini = genai.GenerativeModel(
                model_name=model,
                system_instruction=static_prefix,
            )
            cfg = genai.types.GenerationConfig(temperature=0.1, max_output_tokens=4000)
            
            response = await _with_429_retries(
                lambda: gemini.generate_content_async(task_prompt, generation_config=cfg)
            )
            
            text = response.text
            if response.usage_metadata:
                usage["input_tokens"]  = response.usage_metadata.prompt_token_count
                usage["output_tokens"] = response.usage_metadata.candidates_token_count

        # ─────────────────── Anthropic (cache_control) ──────────────────
        elif provider == "anthropic":
            system_block = {
                "type": "text",
                "text": static_prefix,
                "cache_control": {"type": "ephemeral"},
            }

            # crude token estimate: words×1.2  (safe over-count)
            est_tokens = math.ceil(1.2 * len(static_prefix.split()))
            await _anthropic_throttle(est_tokens)

            response = await anthropic_client_async.messages.create(
                model=model,
                max_tokens=4000,
                temperature=0.1,
                system=[system_block],
                messages=[{"role": "user", "content": task_prompt}],
            )
            text = response.content[0].text
            usage["input_tokens"]   = response.usage.input_tokens
            usage["output_tokens"]  = response.usage.output_tokens
            usage["cached_tokens"]  = response.usage.cache_read_input_tokens

        # ─────────────────── OpenAI (auto prompt cache) ─────────────────
        elif provider == "openai":
            msgs = [
                {"role": "system", "content": static_prefix},
                {"role": "user",   "content": task_prompt},
            ]
            rsp = await openai_client_async.chat.completions.create(
                model=model,
                messages=msgs,
                temperature=0.1,
                max_tokens=4000,
            )
            text = rsp.choices[0].message.content
            usage["input_tokens"]  = rsp.usage.prompt_tokens
            usage["output_tokens"] = rsp.usage.completion_tokens
            try:
                details = rsp.usage.prompt_tokens_details
                usage["cached_tokens"] = details.get("cached_tokens", 0)
            except AttributeError:
                usage["cached_tokens"] = 0

        else:
            raise ValueError(f"Unknown provider {provider}")

        return text, usage


# --- 4. Parallel Orchestration Function ---

# ────────────────────────────────────────────────────────────────────
#  Parallel across PROBLEMS, but seed Anthropic cache with the first
#  problem before launching the rest.
# ────────────────────────────────────────────────────────────────────
async def generate_GSM8K_code_parallel(
    model_dict: Dict[str, List[str]],
    indices_to_generate: List[int],
    example_indices: List[int],
    output_dir: Path = BASE_OUTPUT_DIR,
    max_parallel_problems: int | None = None,      # None = unlimited
) -> pd.DataFrame:
    # choose a unique run-id right at the start  ────────────────────────
    run_ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d_%H%M%S")
    output_dir.mkdir(parents=True, exist_ok=True)
    provider_sems = {
        prov: asyncio.Semaphore(limit) for prov, limit in API_CONCURRENCY_LIMITS.items()
    }
    problem_sem = (
        asyncio.Semaphore(max_parallel_problems)
        if max_parallel_problems is not None
        else None
    )

    static_prefix = STATIC_PREFIX
    rows: list[dict] = []

    # ── coroutine for a single GSM8K problem ──────────────────────────
    async def _run_one_problem(idx: int):
        async def _guard():
            nonlocal rows
            task_prompt = build_task_prompt(idx)
            p_dir = output_dir / str(idx)
            p_dir.mkdir(parents=True, exist_ok=True)

            # launch model calls (your inner gather)
            tasks = []
            for prov, models in model_dict.items():
                for m in models:
                    t = asyncio.create_task(
                        call_model_api_async(
                            provider=prov,
                            model=m,
                            static_prefix=static_prefix,
                            task_prompt=task_prompt,
                            semaphore=provider_sems[prov],
                        )
                    )
                    t.meta = {"provider": prov, "model": m, "index": idx, "start": time.time()}
                    tasks.append(t)

            results = await asyncio.gather(*tasks, return_exceptions=True)
            for t, res in zip(tasks, results):
                meta = t.meta
                elapsed = time.time() - meta["start"]
                status = "Failed"
                text = ""
                usage = {"input_tokens": 0, "output_tokens": 0, "cached_tokens": 0}

                if not isinstance(res, Exception):
                    text, usage = res
                    status = "Success"
                    if text:
                        (p_dir / f"{meta['provider']}_{meta['model']}.txt").write_text(
                            text, encoding="utf-8"
                        )
                else:
                    print(f"{meta['provider']}_{meta['model']} ❌ {res}")

                rows.append(
                    {
                        "provider": meta["provider"],
                        "model": meta["model"],
                        "index": meta["index"],
                        "status": status,
                        "time_s": round(elapsed, 3),
                        "utc_completed": datetime.datetime.utcnow().isoformat(timespec="seconds"),
                        "input_tokens": usage["input_tokens"],
                        "output_tokens": usage["output_tokens"],
                        "cached_tokens": usage["cached_tokens"],
                    }
                )

        return await _guard() if problem_sem is None else await problem_sem.__aenter__() or await _guard() or await problem_sem.__aexit__(None, None, None)

    # ── 1. Seed cache with the FIRST index (blocking) ─────────────────
    first_idx, *rest = indices_to_generate
    await _run_one_problem(first_idx)

    # ── 2. Fan-out remaining problems concurrently ────────────────────
    await asyncio.gather(*[_run_one_problem(i) for i in rest])

    # ── save CSV ─────────────────────────────────────────────────────
    df = pd.DataFrame(rows)
    csv_path = output_dir / f"generation_performance_{run_ts}.csv"
    df.to_csv(csv_path, index=False)
    print(f"✓ All done — log at {csv_path}")
    return df


# --- 5. Code Cleaning and Output Processing ---

# Matches  ```python … ```  or  ```py … ```  (any EOL style)
_CODE_BLOCK_RE = re.compile(
    r"```(?:python|py)\s*\r?\n(.*?)\r?\n```",
    re.DOTALL | re.IGNORECASE,
)

def process_and_clean_outputs(
    source_dir: Path | str = BASE_OUTPUT_DIR,
    dest_dir:   Path | str = PROJECT_ROOT / "data" / "code_gen_outputs_cleaned",
):
    """
    Traverses `source_dir`, cleans raw .txt model outputs, and writes them as
    .py files to `dest_dir`, preserving the relative folder structure.

    Steps performed
    ---------------
    1.  Walk through every sub-directory of `source_dir`.
    2.  Detect all files that end with `.txt`.
    3.  Build the matching sub-directory path in `dest_dir`.
    4.  Read the .txt and extract code inside a markdown fence:
            ```python
            <code>
            ```
        – If no fence is found, the whole file is used as is.
    5.  Write the cleaned code to `<same_name>.py` in the destination tree.
    6.  Leave the original raw files untouched.
    """
    # Resolve to absolute paths
    source_dir = Path(source_dir).expanduser().resolve()
    dest_dir   = Path(dest_dir).expanduser().resolve()

    print(f"Starting processing from: {source_dir}")
    print(f"Cleaned files will be saved in: {dest_dir}\n")

    if not source_dir.is_dir():
        print(f"Error: Source directory '{source_dir}' not found.")
        return

    files_processed = 0

    # 1. Walk through every *.txt under source_dir
    for txt_path in source_dir.rglob("*.txt"):

        try:
            # 2. Derive the destination sub-folder (Step 3)
            rel_path   = txt_path.parent.relative_to(source_dir)
            dest_subdir = dest_dir / rel_path
            dest_subdir.mkdir(parents=True, exist_ok=True)

            # 3. Read raw content (Step 4)
            raw_content = txt_path.read_text(encoding="utf-8")

            match = _CODE_BLOCK_RE.search(raw_content.lstrip())
            if match:
                cleaned_code = match.group(1).strip()
                print(f"✓ extracted code block → {txt_path}")
            else:
                cleaned_code = raw_content.strip()
                print(f"⚠ no code block; using full file → {txt_path}")

            # 4. Write to .py in destination (Step 5)
            dest_file = dest_subdir / f"{txt_path.stem}.py"
            dest_file.write_text(cleaned_code, encoding="utf-8")
            files_processed += 1

        except Exception as e:
            print(f"❌ error processing {txt_path}: {e}")

    # 5. Summary (Step 6)
    print(f"\nProcessing complete — {files_processed} files written.")
