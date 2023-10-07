import os
from datetime import datetime

root_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_dir, "file_info.txt")

with open(file_path, "a") as file:
    pass

file_info = os.stat(file_path)
#General information:
print(file_info)

#Precise information:
print(f"File size: {file_info.st_size} bytes.")
print(f"Last modified: {datetime.fromtimestamp(int(file_info.st_mtime))}")
