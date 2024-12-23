import os
from color_codes import *

directory = "/media/kali/256"

for dirpath, dirnames, filenames in os.walk(f"{directory}"):
    print_ic(f"\nCurrent Directory: {dirpath}", RED, BOLD)
    print_ic(f"Subdirectories: {dirnames}", CYAN)
    print(f"Files: {filenames}")
