import os
import shutil

# 1. Define the directory to organize
# '.' means the current folder where this script is saved
# You can change this to a specific path like r"C:\Users\Gaviru\Downloads" later
TARGET_DIR = '.' 

# 2. Define the rules: Which extensions go to which folder?
DIRECTORIES = {
    "IMAGES": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "DOCUMENTS": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "SETUP_FILES": [".exe", ".msi", ".bat"],
    "VIDEOS": [".mp4", ".mkv", ".avi"]
}

def organize_files():
    print(f"--- Scanning directory: {os.path.abspath(TARGET_DIR)} ---")
    
    # Get all files in the directory
    files = os.listdir(TARGET_DIR)
    
    for file in files:
        # Get the file extension (e.g., '.jpg')
        filename, extension = os.path.splitext(file)
        extension = extension.lower() # Make it lowercase to be safe
        
        # Skip this python script itself so we don't move it!
        if file == "organizer.py":
            continue

        # Check if it matches our rules
        moved = False
        for folder_name, extensions_list in DIRECTORIES.items():
            if extension in extensions_list:
                # 3. Create the folder if it doesn't exist
                folder_path = os.path.join(TARGET_DIR, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                    print(f"Created new folder: {folder_name}")

                # 4. Move the file
                old_path = os.path.join(TARGET_DIR, file)
                new_path = os.path.join(folder_path, file)
                
                try:
                    shutil.move(old_path, new_path)
                    print(f"MOVED: {file} -> {folder_name}/")
                    moved = True
                except Exception as e:
                    print(f"ERROR moving {file}: {e}")
                
                break # Stop checking other folders if we found a match

    print("--- Organization Complete ---")

if __name__ == "__main__":
    organize_files()
