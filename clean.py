import os

def deleteFolder(folder_path):
    if os.path.exists(folder_path):
        # Iterate over all files and subfolders in the "tags" directory
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                os.remove(file_path)  # Remove files
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                os.rmdir(dir_path)  # Remove subfolders
        os.rmdir(folder_path)  # Remove the main "tags" folder
        print(f"Deleted {folder_path} and its contents.")
    else:
        print(f"{folder_path} does not exist.")
