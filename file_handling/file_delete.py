import os

root_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_dir, "my_first_file.txt")

if os.path.isfile(file_path):
    os.remove(file_path)
else:
    print("File already deleted!")