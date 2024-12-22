import os

directory = "/media/kali/256"
for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    if os.path.isfile(file_path):  # Only process files
        with open(file_path, "r") as f:
            content = f.read()
            print(f"Contents of {file_path}:\n{content}")
