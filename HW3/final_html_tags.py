import os

folder_path = "html_tags"

for filename in os.listdir(folder_path):
    
    if "html_tags_" in filename:
        
        new_filename = filename.replace("html_tags_", "")
        
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
