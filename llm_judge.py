# llm_judge_sync.py  

"""
LLM-based reasoning checker.
Reads a JSONL of rows that have ALREADY passed numeric judging and
outputs two files:
  *_reasoning_ok.jsonl
  *_reasoning_rejects.jsonl
"""


import json
from pathlib import Path
import openai

MODEL = "gpt-4o-mini"

SYSTEM_MSG = (
    "You are a strict grader. A student intentionally makes a described "
    "algebra mistake. Look ONLY at the reasoning steps and answer YES if the "
    "steps match the described mistake, otherwise NO."
)

FEW_SHOT = [
    # -- SWAP_RHS — YES
    {
        "role": "user",
        "content": (
            "TEMPLATE: swap right-hand-side constants\n\n"
            "STEPS:\n2x + y = 7   ← swapped\n3x - 4y = 5   ← swapped"
        ),
    },
    {"role": "assistant", "content": "YES"},
    # -- SWAP_RHS — NO
    {
        "role": "user",
        "content": (
            "TEMPLATE: swap right-hand-side constants\n\n"
            "STEPS:\n2x + y = 5   ← original\n3x - 4y = 7   ← original"
        ),
    },
    {"role": "assistant", "content": "NO"},
    # (add similar YES/NO pairs for other templates) …
]

def reasoning_ok(template_desc: str, steps: str, client) -> bool:
    msgs = (
        [{"role": "system", "content": SYSTEM_MSG}]
        + FEW_SHOT
        + [
            {
                "role": "user",
                "content": (
                    f"TEMPLATE: {template_desc}\n\n"
                    f"STEPS:\n{steps}\n\n"
                    "Respond with a single word: YES or NO."
                ),
            }
        ]
    )
    resp = client.chat.completions.create(
        model=MODEL, messages=msgs, temperature=0, max_tokens=1
    )
    return resp.choices[0].message.content.strip().upper() == "YES"


def run_llm_judge(src_path: Path):
    ok_path  = src_path.with_name(src_path.stem + "_reasoning_ok.jsonl")
    bad_path = src_path.with_name(src_path.stem + "_reasoning_rejects.jsonl")

    client = openai.OpenAI()  # uses your OPENAI_API_KEY from env

    keep = toss = 0
    with src_path.open() as src, ok_path.open("w") as okf, bad_path.open("w") as badf:
        for line in src:
            row = json.loads(line)
            if reasoning_ok(row["template_description"], row["answer_steps"], client):
                okf.write(line)
                keep += 1
            else:
                badf.write(line)
                toss += 1

    print(
        f"LLM judge done: {keep} OK  |  {toss} rejects "
        f"→  {ok_path.name}, {bad_path.name}"
    )
