import json
import os
from color_codes import *

directory = "/media/kali"
log_crawl = "drive_crawler_log.txt"

tree = {}

for dirpath, dirnames, filenames in os.walk(f"{directory}"):
    # print_ic(f"\nCurrent Directory: {dirpath}", RED, BOLD)
    # print_ic(f"\tSubdirectories: {dirnames}", CYAN)
    # print(f"\t\tFiles: {filenames}")
    #
    # if len(filenames) == 0:
    #     tree.update(
    #         {
    #             dirpath : {
    #                 directory: filenames for directory in dirnames
    #             }
    #         }
    #     )
    parts = dirpath.split(os.sep)
    subtree = tree
    for part in parts:
        subtree = subtree.setdefault(part, {})
    subtree.update({"_files": filenames})

    # with open(log_crawl, "a") as drive:
    #     drive.write(f"\nCurrent Directory: {dirpath}")
    #     drive.write(f"\n\tSubdirectories: {dirnames}")
    #     drive.write(f"\n\t\tFiles: {filenames}")

with open("tree.json", "w") as json_file:
    json.dump(tree, json_file, indent=4)
