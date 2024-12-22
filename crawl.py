import os
from color_codes import *

directory = "/media/kali/256"
for dir_list in os.listdir(directory):
    if os.path.isdir(f"{directory}/{dir_list}"):
        print_ic(f"Folders in drive: {directory}/ {dir_list}", BLUE, REVERSE)
    else:
        print_ic(f"Files in drive: {directory}/ {dir_list}")
