import os

directory = "/media/kali/256"
for file in os.listdir(directory):
    print(f"In drive: {directory}/ {file}")
