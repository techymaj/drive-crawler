import os
from color_codes import *

directory = "/media/kali/256"
for dir_list in os.listdir(directory):
    if os.path.isdir(f"{directory}/{dir_list}"):
        for dirpath, dirnames, filenames in os.walk(f"{directory}/{dir_list}"):
            print_ic(f"\nCurrent Directory: {dirpath}", RED, BOLD)
            print_ic(f"Subdirectories: {dirnames}", CYAN)
            print(f"Files: {filenames}")
