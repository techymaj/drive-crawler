import os
from color_codes import *

directory = "/media/kali/256"
for dir_list in os.listdir(directory):
    if os.path.isdir(f"{directory}/{dir_list}"):
        print_ic(f"In drive: {directory}/ {dir_list}")
