import os
import shutil


# Base directories
#Specify the file path you wish to use as a source and where you want it
source_dir = r"C:\Users\NAMEHERE\AppData\Local\BeamNG\BeamNG.drive\current\mods"
target_dir = r"C:\Users\NAMEHERE\AppData\Local\BeamNG\BeamNG.drive\current\mods"

# Walk through all files in source_dir
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # File extensions and patterns to match
        if file.endswith(".pc") or file.endswith(".jpg") or (file.endswith(".json") and file.startswith("info")):
            # Calculate the relative path
            rel_path = os.path.relpath(root, source_dir)
            # Create the destination folder structure in target_dir
            dest_folder = os.path.join(target_dir, rel_path)
            os.makedirs(dest_folder, exist_ok=True)
            # Copy the file
            shutil.move(os.path.join(root, file), os.path.join(dest_folder, file))
            print(f"Copied: {file} to {dest_folder}")

