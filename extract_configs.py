import os
import shutil

# Base directories
source_dir = r"C:\Users\xpogo\AppData\Local\BeamNG\BeamNG.drive\current\mods\unpacked\agenty_global_values_tuning"
target_dir = r"C:\Users\xpogo\AppData\Local\BeamNG\BeamNG.drive\current\mods\unpacked\agenty_global_values_tuning\configs"

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
