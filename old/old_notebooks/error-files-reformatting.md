```python
from pathlib import Path
import json

# --- Path and Directory Definitions ---
def find_project_root(marker: str = ".git") -> Path:
    current_path = Path.cwd().resolve()
    while current_path != current_path.parent:
        if (current_path / marker).exists():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError(f"Could not find project root. Marker '{marker}' not found.")

PROJECT_ROOT = find_project_root()
DATA_DIR = PROJECT_ROOT / 'data'

# Yewei
DIR_1001_1500_COMPUTATIONAL = PROJECT_ROOT / 'yewei' / 'gsm8k_data' / 'computational'
DIR_1001_1500_CONCEPTUAL = PROJECT_ROOT / 'yewei' / 'gsm8k_data' / 'conceptual'

# Ling
DIR_1500_1599_CONCEPTUAL = DATA_DIR

# Mauro
DIR_500_999_MIXED = DATA_DIR / 'manually_gen_incorrect_answers_gsm8k'

# Ali
DIR_0_400_MIXED = PROJECT_ROOT / 'GSM8_Edited'

# Check if all the directories exist
for directory in [
    DIR_1001_1500_COMPUTATIONAL,
    DIR_1001_1500_CONCEPTUAL,
    DIR_1500_1599_CONCEPTUAL,
    DIR_500_999_MIXED,
    DIR_0_400_MIXED
]:
    if not directory.exists():
        print(f"Directory does not exist: {directory}")


filepaths = {
    # Yewei
    "1001_1500_computational": DIR_1001_1500_COMPUTATIONAL / "gsm8k_augmented_1001_1100_computational.json",
    "1001_1500_conceptual": DIR_1001_1500_CONCEPTUAL / "gsm8k_augmented_1001_1100_conceptual.json",
    "1101_1200_computational": DIR_1001_1500_COMPUTATIONAL / "gsm8k_augmented_1101_1200_computational.json",
    "1101_1200_conceptual": DIR_1001_1500_CONCEPTUAL / "gsm8k_augmented_1101_1200_conceptual.json",
    "1201_1300_computational": DIR_1001_1500_COMPUTATIONAL / "gsm8k_augmented_1201_1300_computational.json",
    "1201_1300_conceptual": DIR_1001_1500_CONCEPTUAL / "gsm8k_augmented_1201_1300_conceptual.json",
    "1301_1400_computational": DIR_1001_1500_COMPUTATIONAL / "gsm8k_augmented_1301_1400_computational.json",
    "1301_1400_conceptual": DIR_1001_1500_CONCEPTUAL / "gsm8k_augmented_1301_1400_conceptual.json",
    "1401_1500_computational": DIR_1001_1500_COMPUTATIONAL / "gsm8k_augmented_1401_1500_computational.json",
    "1401_1500_conceptual": DIR_1001_1500_CONCEPTUAL / "gsm8k_augmented_1401_1500_conceptual.json",

    # Ling
    "1500_1599_conceptual": DIR_1500_1599_CONCEPTUAL / "1500_1599_conceptual.jsonl",

    # Mauro
    "500_999_mixed": DIR_500_999_MIXED / "gsm8k_annotated_500_to_999.jsonl",

    # Ali
    "0_100_mixed": DIR_0_400_MIXED / "0-100.json",
    "101-200_mixed": DIR_0_400_MIXED / "101-200.json",
    "201-300_mixed": DIR_0_400_MIXED / "201_to_300.json",
    "301-400_mixed": DIR_0_400_MIXED / "301_to_400.json"
}

# Output dir for the merged jsonl file
OUTPUT_DIR = DATA_DIR

# Load all files into a single dictionary
all_data = {}
for key, filepath in filepaths.items():
    try:
        with open(filepath) as f:
            if filepath.suffix == ".jsonl":
                # Handle JSONL files
                all_data[key] = [json.loads(line) for line in f]
            else:
                # Handle JSON files
                all_data[key] = json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")


from datasets import load_dataset

GSM8K_TRAIN = load_dataset("gsm8k", "main", split="train")

```


```python
import re
import json
from pathlib import Path
from typing import Dict, List, Union, Optional
from datasets import Dataset

def extract_start_index(key: str) -> int:
    """
    Given a key like "1001_1500_conceptual" or "101-200_mixed",
    return the first integer (e.g. 1001 or 101).
    """
    m = re.search(r"(\d+)", key)
    if not m:
        raise ValueError(f"No integer start index found in key '{key}'")
    return int(m.group(1))

def build_question_index_map(dataset: Dataset) -> Dict[str, int]:
    """
    Build a dict mapping each question string to its index in the GSM8K train split.
    """
    return {
        sample["question"].strip(): idx
        for idx, sample in enumerate(dataset)
    }

def merge_augmented_data(
    all_data: Dict[str, Union[List[dict], dict]],
    filepaths: Dict[str, Path],
    gsm8k_train: Dataset,
    output_dir: Union[str, Path],
    project_root: Path,
    output_filename: str = "manually_generated_errors.jsonl"
) -> None:
    """
    Merge all of your JSON/JSONL files into a single JSONL, adding:
      - "index": the example’s index in the GSM8K train split
      - "filepath": the source filepath, made relative to project_root

    Args:
        all_data:       mapping from your file-key (e.g. "0_100_mixed") to list or dict of records
        filepaths:      same keys → Path to each original JSON/JSONL file
        gsm8k_train:    the HuggingFace Dataset for "gsm8k" train split
        output_dir:     directory in which to write the merged JSONL
        project_root:   Path to your project root, used to relativize filepaths
        output_filename: name of the output JSONL file (default: "merged_augmented_data.jsonl")
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / output_filename

    # build question → index lookup
    q2idx = build_question_index_map(gsm8k_train)

    total_written = 0
    with open(out_path, "w", encoding="utf-8") as fout:
        for key, records in all_data.items():
            records_list = records if isinstance(records, list) else [records]
            start_idx = extract_start_index(key)
            src_path: Optional[Path] = filepaths.get(key)

            # compute filepath relative to project_root (or fallback)
            if src_path is not None:
                try:
                    rel_fp = src_path.relative_to(project_root)
                except ValueError:
                    rel_fp = src_path
            else:
                rel_fp = Path(key)

            for i, rec in enumerate(records_list):
                q = rec.get("question", "").strip()
                idx = q2idx.get(q, start_idx + i)
                merged = {
                    **rec,
                    "index": idx,
                    "filepath": rel_fp.as_posix()
                }
                fout.write(json.dumps(merged, ensure_ascii=False) + "\n")
                total_written += 1

    print(f"Merged {total_written} records → {out_path}")
```


```python
merge_augmented_data(
    all_data=all_data,
    filepaths=filepaths,
    gsm8k_train=GSM8K_TRAIN,
    output_dir=OUTPUT_DIR,
    project_root=PROJECT_ROOT
)
```

    Merged 1963 records → /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/manually_generated_errors.jsonl



```python
import json
from datasets import load_dataset
from pathlib import Path
from typing import Optional

def verify_merged_jsonl(
    jsonl_path: Path,
    gsm8k_train=None,
    max_display: int = 10
) -> None:
    """
    Verify that each 'question' in the merged JSONL matches the
    GSM8K train split question at the recorded 'index'.

    Args:
        jsonl_path:    Path to your merged_augmented_data.jsonl
        gsm8k_train:   (optional) pre-loaded Dataset; if None, we'll load it for you
        max_display:   number of mismatches to print in detail
    """
    # 1) load GSM8K if not provided
    if gsm8k_train is None:
        gsm8k_train = load_dataset("gsm8k", "main", split="train")

    total = 0
    mismatches = []

    # 2) iterate merged file
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            total += 1
            rec = json.loads(line)
            idx = rec.get("index")
            merged_q = rec.get("question", "").strip()

            # 3) fetch original
            try:
                orig_q = gsm8k_train[idx]["question"].strip()
            except (IndexError, KeyError, TypeError):
                mismatches.append((total, idx, merged_q, None))
                continue

            # 4) compare
            if merged_q != orig_q:
                mismatches.append((total, idx, merged_q, orig_q))

    # 5) report
    print(f"Checked {total} records.")
    if not mismatches:
        print("✅ All questions match the GSM8K dataset.")
    else:
        print(f"⚠️  Found {len(mismatches)} mismatches:")
        for record_num, idx, merged_q, orig_q in mismatches[:max_display]:
            print(f"\n  • Record #{record_num} (index={idx}):")
            print(f"      Merged : {merged_q!r}")
            if orig_q is None:
                print("      Original: <index out of range>")
            else:
                print(f"      Original: {orig_q!r}")
        if len(mismatches) > max_display:
            print(f"\n  ...plus {len(mismatches)-max_display} more.")
```


```python
verify_merged_jsonl(
    jsonl_path=OUTPUT_DIR / "manually_generated_errors.jsonl",
    gsm8k_train=GSM8K_TRAIN,
    max_display=10
)
```

    Checked 1963 records.
    ⚠️  Found 9 mismatches:
    
      • Record #1003 (index=1502):
          Merged : "Dani brings two and half dozen cupcakes for her 2nd-grade class.  There are 27 students (including Dani), 1 teacher, and 1 teacher's aid.  If 3 students called in sick that day, how many cupcakes are left after Dani gives one to everyone in the class?"
          Original: 'Dani brings two and half dozen cupcakes for her 2nd-grade class.  There are 27 students (including Dani), 1 teacher, and 1 teacher’s aid.  If 3 students called in sick that day, how many cupcakes are left after Dani gives one to everyone in the class?'
    
      • Record #1014 (index=1513):
          Merged : "Tom's cat is 8 years old.  His rabbit is half the age of his cat.  His dog is three times as old as his rabbit.  How old is the dog?"
          Original: 'Tom’s cat is 8 years old.  His rabbit is half the age of his cat.  His dog is three times as old as his rabbit.  How old is the dog?'
    
      • Record #1029 (index=1528):
          Merged : "Gabby is saving money to buy a new makeup set. The makeup set costs $65 and she already has $35. Gabby's mom gives her an additional $20. How much money does Gabby need to buy the set?"
          Original: 'Gabby is saving money to buy a new makeup set. The makeup set costs $65 and she already has $35. Gabby’s mom gives her an additional $20. How much money does Gabby need to buy the set?'
    
      • Record #1040 (index=1539):
          Merged : "Chris is trying to sell his car for $5200 and has gotten two price offers. One buyer offered to pay the full price if Chris would pay for the car maintenance inspection, which cost a tenth of Chris's asking price. The other buyer agreed to pay the price if Chris replaced the headlights for $80 and the tires for three times as much. What is the difference between the amounts Chris will earn from the two offers?"
          Original: 'Chris is trying to sell his car for $5200 and has gotten two price offers. One buyer offered to pay the full price if Chris would pay for the car maintenance inspection, which cost a tenth of Chris’s asking price. The other buyer agreed to pay the price if Chris replaced the headlights for $80 and the tires for three times as much. What is the difference between the amounts Chris will earn from the two offers?'
    
      • Record #1045 (index=1544):
          Merged : "Ken can do 20 sit-ups without stopping. Nathan can do twice as many, and Bob can do half the number of Ken and Nathan's combined sit-ups. How many more sit-ups can Nathan do compared to Bob?"
          Original: 'Ben will receive a bonus of $1496. He chooses to allocate this amount as follows: 1/22 for the kitchen, 1/4 for holidays and 1/8 for Christmas gifts for his 3 children. How much money will he still have left after these expenses?'
    
      • Record #1057 (index=1556):
          Merged : 'Miss Walter has 50 gold stickers. She also has twice as many silver stickers as gold stickers, and 20 fewer bronze stickers than silver stickers.  She wants to give the same number of stickers to each of her 5 students. How many stickers will one school receive?'
          Original: 'Alyana has a pizza that is cut into 16 slices. After she and her friends finish eating, there are 4 slices left. If each of them ate 2 slices of pizza, how many people ate the pizza?'
    
      • Record #1060 (index=1559):
          Merged : 'Jaynie wants to make leis for the graduation party. It will take 2 and half dozen plumeria flowers to make 1 lei. If she wants to make 4 leis, how many plumeria flowers must she pick from the trees in her yard?'
          Original: 'Maci is planning for the new school year and goes to the store to buy pens. She needs ten blue pens and 15 red pens. If a blue pen costs ten cents each and a red pen costs twice as much as the blue pen, how much money does Maci pay for the pens?'
    
      • Record #1061 (index=1560):
          Merged : 'The Great Pyramid of Giza was the tallest man-made structure on earth for almost 4000 years. It is 20 feet taller than 500 feet, and 234 feet wider than it is tall. What is the sum of the height and width of the Great Pyramid of Giza in feet?'
          Original: 'Yvette wants to frame a new picture. When she goes to her local frame shop, she finds out that the frame she wanted is 20% more expensive than her budget of $60. If she paid for a smaller frame at 3/4 the new price of the frame she initially intended to buy, how much money did she remain with?'
    
      • Record #1962 (index=399):
          Merged : "Sam works at the Widget Factory, assembling Widgets. He can assemble 1 widget every 10 minutes. Jack from the loading dock can help assemble widgets when he doesn't have anything else to do. When he helps, they put together 2 complete widgets every 15 minutes. Recently the factory hired Tony to help assemble widgets. Being new to the job, he doesn't work as fast as Sam or Jack. Yesterday Sam worked for 6 hours before he had to leave work early for a dentist appointment. Jack was able to help out for 4 hours before he had to go back to the loading dock to unload a new shipment of widget materials. Tony worked the entire 8-hour shift. At the end of the day, they had completed 76 widgets. How long does it take Tony to assemble a Widget, in minutes?"
          Original: "Sam works at the Widget Factory, assembling Widgets. He can assemble 1 widget every 10 minutes. Jack from the loading dock can help assemble widgets when he doesn't have anything else to do. When he helps, they put together 2 complete widgets every 15 minutes. Recently the factory hired Tony to help assemble widgets. Being new to the job, he doesn't work as fast as Sam or Jack. Yesterday Sam worked for 6 hours before he had to leave work early for a dentist appointment. Jack was able to help out for 4 hours before he had to go back to the loading dock to unload a new shipment of widget materials. Tony worked the entire 8-hour shift. At the end of the day, they had completed 68 widgets. How long does it take Tony to assemble a Widget, in minutes?"



```python
import unicodedata
import re

def sanitize_text(text: str) -> str:
    """
    Normalize and clean up a solution string for consistent line splitting.

    Steps:
      1. Unicode-normalize to NFC form.
      2. Convert all CRLF or CR line endings to LF.
      3. Strip trailing whitespace on each line.
      4. Remove any zero-width or non-printable characters.
      5. Trim leading/trailing blank lines.

    Args:
        text: raw solution string (may contain weird unicode or mixed line endings)
    Returns:
        cleaned text with uniform LF endings and no extraneous trailing spaces.
    """
    # 1) Unicode normalize
    text = unicodedata.normalize("NFC", text)

    # 2) Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # 3) Strip trailing whitespace and remove non-printables
    #    (e.g. zero-width spaces, etc.)
    def clean_line(line: str) -> str:
        # remove zero-width / control chars except newline
        line = re.sub(r"[\u200B-\u200D\uFEFF]", "", line)
        return line.rstrip()

    lines = [clean_line(ln) for ln in text.split("\n")]

    # 4) Trim leading/trailing blank lines
    while lines and lines[0] == "":
        lines.pop(0)
    while lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines)
```


```python
import re
import json
from pathlib import Path
from typing import Dict, List, Optional, Union
from datasets import Dataset, load_dataset

def build_solution_mapping_from_text_nosanitize(
    solution_text: str,
    exclude_FA: bool = True
) -> Dict[str, str]:
    """
    Split raw solution text into a line-numbered dict, without any sanitization.

    Args:
        solution_text: the full multi-line solution string
        exclude_FA:    if True, drop the final "#### {answer}" line entirely
    Returns:
        mapping of "L1", "L2", … to each non-blank line of solution_text
        (and optionally "FA" if exclude_FA=False)
    """
    lines = [ln.strip() for ln in solution_text.splitlines() if ln.strip()]
    mapping: Dict[str, str] = {}

    # if last line is "#### {digits}" treat as final answer
    if lines and re.match(r"^####\s*[\d\.,]+$", lines[-1]):
        fa_line = lines.pop(-1).strip()
        if not exclude_FA:
            mapping["FA"] = fa_line

    for i, line in enumerate(lines, start=1):
        mapping[f"L{i}"] = line

    return mapping


def compute_first_erroneous_line_nosanitize(
    input_jsonl: Union[str, Path],
    output_jsonl: Optional[Union[str, Path]] = None,
    gsm8k_train: Optional[Dataset] = None
) -> Dict[str, List[int]]:
    """
    Like compute_first_erroneous_line, but uses the nosanitize mapping.

    Returns dict with:
      - correct_answer_mismatch
      - wrong_answer_full_matches
      - wrong_answer_weird

    And (if output_jsonl is set) writes an annotated JSONL with
    'erroneous_line_number' added where appropriate.
    """
    if gsm8k_train is None:
        gsm8k_train = load_dataset("gsm8k", "main", split="train")

    cam, wafm, waw = [], [], []
    annotated: List[dict] = []

    with open(input_jsonl, "r", encoding="utf-8") as fin:
        for raw in fin:
            rec = json.loads(raw)
            idx = rec["index"]

            ans_map   = build_solution_mapping_from_text_nosanitize(rec["answer"])
            wrong_map = build_solution_mapping_from_text_nosanitize(rec["wrong_answer"])
            ds_text   = gsm8k_train[idx]["answer"]
            ds_map    = build_solution_mapping_from_text_nosanitize(ds_text)

            # 1) correct-answer mismatch?
            if ans_map != ds_map:
                cam.append(idx)
                annotated.append(rec)
                continue

            # 2) wrong-answer exactly matches full solution?
            if wrong_map == ds_map:
                wafm.append(idx)
                annotated.append(rec)
                continue

            # find first line where wrong ≠ dataset
            keys = sorted(ds_map.keys(), key=lambda k: int(k[1:]))
            first_diff = next((k for k in keys if wrong_map.get(k) != ds_map.get(k)), None)

            # 3) weird: any later line matches again?
            is_weird = False
            if first_diff:
                start = int(first_diff[1:])
                for k in keys:
                    if int(k[1:]) > start and wrong_map.get(k) == ds_map.get(k):
                        waw.append(idx)
                        is_weird = True
                        break

            if is_weird:
                annotated.append(rec)
                continue

            # 4) normal: annotate the first differing line
            if first_diff:
                rec["erroneous_line_number"] = first_diff
            annotated.append(rec)

    if output_jsonl:
        out = Path(output_jsonl)
        with out.open("w", encoding="utf-8") as fout:
            for rec in annotated:
                fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"Wrote annotated JSONL to {out}")

    return {
        "correct_answer_mismatch": cam,
        "wrong_answer_full_matches": wafm,
        "wrong_answer_weird": waw
    }
```


```python
results = compute_first_erroneous_line_nosanitize(
    input_jsonl= DATA_DIR / "manually_generated_errors.jsonl",
    output_jsonl= DATA_DIR / "manually_generated_errors_final.jsonl"
)

```

    Wrote annotated JSONL to /Users/arvindsuresh/Documents/Github/Erdos-DL-June25-Math/data/manually_generated_errors_final.jsonl



```python
print("Correct answers from manually gen files that don't match GSM8K answers:")
print(results["correct_answer_mismatch"])
print()

print("Wrong answers that fully match GSM8K answers:")
print(results["wrong_answer_full_matches"])
print()

print("Wrong answers that are weird (one line differs, but later lines match):")
print(results["wrong_answer_weird"])
print()
```

    Correct answers from manually gen files that don't match GSM8K answers:
    [1513, 1533, 1539, 1544, 1556, 1557, 1559, 1560, 3, 12, 20, 44, 105, 108, 109, 137, 167, 168, 198, 200, 269, 317, 378, 399]
    
    Wrong answers that fully match GSM8K answers:
    [881]
    
    Wrong answers that are weird (one line differs, but later lines match):
    [1001, 1019, 1028, 1030, 1031, 1033, 1039, 1042, 1054, 1062, 1066, 1068, 1069, 1072, 1073, 1074, 1075, 1085, 1093, 1001, 1010, 1030, 1031, 1066, 1069, 1102, 1112, 1124, 1125, 1131, 1133, 1136, 1140, 1143, 1149, 1152, 1153, 1154, 1156, 1159, 1160, 1163, 1164, 1169, 1192, 1193, 1196, 1122, 1125, 1146, 1149, 1184, 1189, 1196, 1202, 1205, 1206, 1212, 1213, 1219, 1221, 1222, 1225, 1226, 1227, 1229, 1233, 1242, 1250, 1251, 1253, 1256, 1259, 1264, 1267, 1269, 1271, 1274, 1286, 1289, 1292, 1295, 1205, 1219, 1231, 1250, 1251, 1269, 1289, 1292, 1302, 1354, 1361, 1362, 1363, 1364, 1372, 1375, 1379, 1380, 1385, 1391, 1393, 1302, 1334, 1338, 1375, 1385, 1391, 1393, 1408, 1410, 1412, 1413, 1418, 1422, 1428, 1430, 1435, 1436, 1437, 1440, 1444, 1446, 1447, 1448, 1449, 1455, 1456, 1465, 1472, 1473, 1486, 1489, 1499, 1413, 1418, 1428, 1435, 1440, 1446, 1481, 1489, 1508, 1536, 537, 549, 562, 573, 578, 580, 592, 598, 602, 668, 716, 783, 803, 808, 812, 873, 988, 18, 25, 27, 30, 40, 42, 56, 90, 123, 139, 147, 157, 162, 173, 182, 191, 192, 199, 215, 218, 219, 222, 238, 243, 257, 284, 287, 288, 300, 328, 329, 355, 359, 389]
    



```python

```
