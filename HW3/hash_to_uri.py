import os
import re

folder_path = "stopword_coronavirus"

uri_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

num_processed_files = 0
num_unique_filenames = 0
unique_filenames = set()

for filename in os.listdir(folder_path):
    if num_processed_files >= 120 or num_unique_filenames >= 10:
        break
    
    if filename.endswith(".txt") and filename not in unique_filenames:
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            uris = re.findall(uri_pattern, content)
            if uris:
                print("URIs in", filename)
                for uri in uris:
                    print(uri)
            
        num_processed_files += 1
        unique_filenames.add(filename)
        num_unique_filenames = len(unique_filenames)
