import json
import os

directory = "/media/kali"

tree = {}

for dirpath, _, filenames in os.walk(f"{directory}"):
    parts = dirpath.split(os.sep)
    parts.remove("")
    subtree = tree
    for part in parts:
        subtree = subtree.setdefault(part, {})
    subtree.update({"_files": filenames})

with open("tree.json", "w") as json_file:
    json.dump(tree, json_file, indent=4)
