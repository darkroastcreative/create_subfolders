import os
import sys
import math
import shutil

# Declare and initialize a constant representing the maximum number of files to
# include in each subfolder. The script will break up the set of files in the
# target directory into subfolders with up to this many files each.
TARGET_SUBFOLDER_SIZE: int = 250

# Obtain a reference to the folder that the user wants to break down into subfolders.
try:
    root_folder_path: str = sys.argv[1]
except IndexError:
    sys.exit('Root folder path not detected. Please ensure that this script is run with the path to a valid directory included as the first argument (e.g., \'/Users/david/Downloads\').')

# Obtain a list of files in the target folder, excluding hidden files (starting
# with "." like ".DS_Store").
file_list: list[str] = [file for file in os.listdir(root_folder_path) if os.path.isfile(os.path.join(root_folder_path, file)) and not file.startswith('.')]


# Declare and initialize variables representing the number of files in the
# target folder and the number of subfolders to create.
file_list_length: int = len(file_list)
target_subfolder_count: int = math.ceil(file_list_length / TARGET_SUBFOLDER_SIZE)

print(f'{file_list_length} files will be divided into {target_subfolder_count} subfolders.')

# Declare and initialize variables to serve as reference points for which
# subfolder is being created in the series and how many files are in the
# subfolder as each one is populated with files.
subfolder_number: int = 1
subfolder_file_number: int = 1

# Create and populate the desired set of subfolders in the target folder.
for file in file_list:
    if subfolder_file_number == 1:
        os.mkdir(path = os.path.join(root_folder_path, str(subfolder_number)))

    shutil.move(src = os.path.join(root_folder_path, file), dst = os.path.join(root_folder_path, str(subfolder_number), file))

    subfolder_file_number += 1

    if subfolder_file_number > TARGET_SUBFOLDER_SIZE:
        subfolder_number += 1
        subfolder_file_number = 1

print('Done!')