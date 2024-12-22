import os
from color_codes import *

directory = "/media/kali/256"
for dir_list in os.listdir(directory):
    if os.path.isdir(f"{directory}/{dir_list}"):
        for item in os.walk(f"{directory}/{dir_list}"):
            print(item)
        # print_ic(f"Folders in drive: {directory}/ {dir_list}", BLUE)
    else:
        print_ic(f"Files in drive: {directory}/ {dir_list}")
