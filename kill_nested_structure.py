import os
import shutil

base_dir = r"C:\Users\xpogo\Personal Files\BeamNG Projects\vehicle files\a-vehicles-0.37"

# Loop through each vehicle directory
for vehicle_name in os.listdir(base_dir):
    vehicle_root = os.path.join(base_dir, vehicle_name)
    nested_path = os.path.join(vehicle_root, "vehicles", vehicle_name)

    if os.path.isdir(nested_path):
        print(f"Flattening: {nested_path} -> {vehicle_root}")

        # Move everything from nested_path to vehicle_root
        for item in os.listdir(nested_path):
            src = os.path.join(nested_path, item)
            dst = os.path.join(vehicle_root, item)

            # If destination already exists, warn or handle it (optional logic here)
            if os.path.exists(dst):
                print(f"Warning: {dst} already exists. Skipping.")
                continue

            shutil.move(src, dst)

        # Remove empty nested folders
        try:
            os.rmdir(nested_path)  # ...\vehicles\<vehicle>
            os.rmdir(os.path.join(vehicle_root, "vehicles"))  # ...\vehicles
            print(f"Cleaned up: {nested_path}")
        except OSError as e:
            print(f"Cleanup failed: {e}")
