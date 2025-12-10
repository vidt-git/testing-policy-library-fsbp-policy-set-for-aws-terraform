import os
import shutil

sentinel_files = []
for root, dirs, files in os.walk('policies'):
    for file in files:
        if file.endswith('.sentinel'):
            sentinel_files.append(os.path.join(root, file))

workspace_root = os.path.dirname(os.path.abspath(__file__))

for path in sentinel_files:
    dest_path = os.path.join(workspace_root, os.path.basename(path))
    if not os.path.exists(dest_path):
        shutil.move(path, dest_path)
        print(f"Moved: {path} -> {dest_path}")
    else:
        print(f"Skipped (already exists): {dest_path}")