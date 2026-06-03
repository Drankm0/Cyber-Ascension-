import os
import shutil

folder = os.path.expanduser("~/Downloads")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Archives": [".zip", ".tar", ".gz"],
}

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        ext = os.path.splitext(filename)[1].lower()
        for folder_name, extensions in file_types.items():
            if ext in extensions:
                dest = os.path.join(folder, folder_name)
                os.makedirs(dest, exist_ok=True)
                shutil.move(filepath, os.path.join(dest, filename))
                print(f"Moved: {filename} → {folder_name}") 
