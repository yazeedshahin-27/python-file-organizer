"""
Python File Organizer
Author: Yazeed Shahin
Description: Organizes files into folders based on file extension.
"""
import os
import shutil

# Path to the folder you want to organize
SOURCE_DIR = "files_to_organize"

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Code": [".py", ".cpp", ".c", ".java"],
}

def create_folders():
    for folder in FILE_TYPES:
        if not os.path.exists(folder):
            os.makedirs(folder)
    if not os.path.exists("Others"):
        os.makedirs("Others")

def organize_files():
    for file in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, file)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file.lower().endswith(tuple(extensions)):
                    shutil.move(file_path, folder)
                    moved = True
                    break

            if not moved:
                shutil.move(file_path, "Others")

if __name__ == "__main__":
    create_folders()
    organize_files()
    print("Files organized successfully!")
