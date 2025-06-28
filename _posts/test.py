import os
import shutil

source_folder = "D:/[3]other/new_folder"
destination_folders = {
    "Images1": [".jpg", ".png", ".gif"],
    "Documents1": [".pdf", ".docx", ".txt"],
    "Videos1": [".mp4", ".mov", ".avi"],
    "Archives1": [".zip", ".rar"],
    "Programs1": [".exe", ".msi" ],
    "Music1": [".mp3"]
}

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        for folder, extensions in destination_folders.items():
            if any(file.endswith(ext) for ext in extensions):
                os.makedirs(os.path.join(source_folder, folder), exist_ok=True)
                shutil.move(file_path, os.path.join(source_folder, folder))