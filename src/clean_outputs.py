import os
import re
import shutil

def process_and_clean_outputs(
    source_dir: str = 'code_generation_outputs',
    dest_dir: str = 'code_generation_outputs_cleaned'
):
    """
    Traverses a source directory, cleans raw .txt model outputs, and saves
    them as .py files in a new destination directory with the same structure.

    This function will:
    1. Walk through all subdirectories of the source_dir.
    2. Find all files ending in .txt.
    3. Create a corresponding subdirectory in the dest_dir.
    4. Read the .txt content and extract the Python code from ```python ... ``` blocks.
    5. Save the cleaned code to a new file with a .py extension in the destination.
    6. The original source directory and its files will be left untouched.

    Args:
        source_dir: The top-level directory containing the raw generated outputs.
        dest_dir: The top-level directory where cleaned .py files will be saved.
    """
    print(f"Starting processing from '{source_dir}'...")
    print(f"Cleaned files will be saved in '{dest_dir}'.")
    files_processed = 0

    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' not found.")
        return

    # os.walk efficiently traverses the entire directory tree
    for dirpath, _, filenames in os.walk(source_dir):
        for filename in filenames:
            # Process only the .txt files
            if filename.endswith(".txt"):
                source_filepath = os.path.join(dirpath, filename)
                print(f"\nProcessing file: {source_filepath}")

                try:
                    # 1. Determine the new directory structure
                    # Replaces 'code_generation_outputs' with 'code_generation_outputs_cleaned'
                    # The '1' ensures it only replaces the first occurrence at the beginning
                    dest_subdir = dirpath.replace(source_dir, dest_dir, 1)
                    
                    # 2. Create the destination subdirectory if it doesn't exist
                    os.makedirs(dest_subdir, exist_ok=True)
                    
                    # 3. Read the raw content from the source file
                    with open(source_filepath, 'r', encoding='utf-8') as f:
                        raw_content = f.read()

                    # 4. Extract the code from the markdown block
                    cleaned_code = ""
                    code_match = re.search(r"```python\n(.*?)\n```", raw_content, re.DOTALL)
                    
                    if code_match:
                        cleaned_code = code_match.group(1).strip()
                        print("  Successfully extracted code from markdown block.")
                    else:
                        cleaned_code = raw_content.strip()
                        print("  Warning: No python markdown block found. Using raw content as code.")

                    # 5. Define the new .py filename and full path
                    base_name = os.path.splitext(filename)[0]
                    py_filename = f"{base_name}.py"
                    dest_filepath = os.path.join(dest_subdir, py_filename)

                    # 6. Write the cleaned code to the new .py file in the destination
                    with open(dest_filepath, 'w', encoding='utf-8') as f:
                        f.write(cleaned_code)
                    print(f"  Saved cleaned code to: {dest_filepath}")
                    
                    files_processed += 1

                except Exception as e:
                    print(f"  An error occurred while processing {source_filepath}: {e}")

    print(f"\nProcessing complete. Processed {files_processed} files.")

if __name__ == '__main__':
    process_and_clean_outputs()