import os

folder_path = "main_text"

for filename in os.listdir(folder_path):
    
    if "main_text_" in filename:
        
        new_filename = filename.replace("main_text_", "")
        
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
