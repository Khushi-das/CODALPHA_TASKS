import os
import shutil

# Set the directory you want to organize
directory = r'C:\Users\khush\OneDrive\Documents'  # Change to your path

# Create folders for file types
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv"],
    "Others": []
}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in file_types.items():
            if any(filename.endswith(ext) for ext in extensions):
                folder_path = os.path.join(directory, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, filename))
                moved = True
                break
        if not moved:
            other_path = os.path.join(directory, "Others")
            os.makedirs(other_path, exist_ok=True)
            shutil.move(file_path, os.path.join(other_path, filename))

print("File organization complete.")