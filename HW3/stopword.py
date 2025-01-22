import os
import shutil

root_folder = "main_text"

output_folder = "stopword_coronavirus"

keyword = "coronavirus"

def file_contains_keyword(file_path, keyword):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        if keyword in content:
            return True
    return False

for dirpath, dirnames, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.endswith(".txt"):
            file_path = os.path.join(dirpath, filename)
            if file_contains_keyword(file_path, keyword):
                output_file_path = os.path.join(output_folder, filename)
                shutil.move(file_path, output_file_path)
                print("Moved file:", filename)
