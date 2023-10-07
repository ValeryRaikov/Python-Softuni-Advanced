import os

root_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "tet.txt"
file_path = os.path.join(root_dir, file_name)

if os.path.isfile(file_path):
    with open(file_path, "r") as file:
        print("File found!")
else:
    print("File not found!")
    raise Exception("Opening error!")