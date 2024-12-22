import os

directory = "/media/kali/256"
for file in os.listdir(directory):
    if os.path.isfile(file):
        print(f"File: {file}")
    else:
        print(f"Directory: {file}")
