import os
import sys
import math
import shutil

TARGET_SUBFOLDER_SIZE: int = 250

try: 
    root_folder_path: str = sys.argv[1]
except IndexError:
    sys.exit('Root folder path not detected. Please ensure that this script is run with the path to a valid directory included as the first argument (e.g., \'/Users/david/Downloads\').')

file_list: list[str] = [file for file in os.listdir(root_folder_path) if os.path.isfile(os.path.join(root_folder_path, file)) and not file.startswith('.')]

file_list_length: int = len(file_list)
target_subfolder_count: int = math.ceil(file_list_length / TARGET_SUBFOLDER_SIZE)

print(f'{file_list_length} files will be divided into {target_subfolder_count} subfolders.')

subfolder_number: int = 1
subfolder_file_number: int = 1

for file in file_list:
    if subfolder_file_number == 1:
        os.mkdir(path = os.path.join(root_folder_path, str(subfolder_number)))

    shutil.move(src = os.path.join(root_folder_path, file), dst = os.path.join(root_folder_path, str(subfolder_number), file))

    subfolder_file_number += 1

    if subfolder_file_number > TARGET_SUBFOLDER_SIZE:
        subfolder_number += 1
        subfolder_file_number = 1

print('Done!')