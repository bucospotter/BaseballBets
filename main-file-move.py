import os
import shutil
import re

# Define the source and destination paths
source_folder = r'C:\Users\boydh\PycharmProjects\BaseballBets'
destination_folder = r'D:\BaseballBetsData7'  # Change E: to your thumb drive letter

# Define your regex pattern for filenames starting with 4 digits followed by an underscore
pattern = r'^\d{4}_'

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Move files
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if re.match(pattern, file):  # Check if the file matches the regex
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_folder, file)

            try:
                # Copy the file and then delete the original
                shutil.copy2(source_file, destination_file)  # Use copy2 to preserve metadata
                os.remove(source_file)
                print(f"Moved: {file}")
            except PermissionError:
                print(f"Permission denied for: {source_file}")
            except OSError as e:
                print(f"Error moving file {file}: {e}")

print("File move operation completed.")
