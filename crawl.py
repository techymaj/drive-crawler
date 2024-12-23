import os
from color_codes import *

path = "/media/kali/256"

with os.scandir(path) as entries:
    for entry in entries:
        name = entry.name
        dir_path = entry.path
        print(f"Name: {name}")
        print(f"Path: {path}")
        print("-" * 80)

        for dirpath, dirnames, filenames in os.walk(f"{dir_path}"):
            print_ic(f"\nCurrent Directory: {dirpath}", RED, BOLD)
            print_ic(f"Subdirectories: {dirnames}", CYAN)
            print(f"Files: {filenames}")
