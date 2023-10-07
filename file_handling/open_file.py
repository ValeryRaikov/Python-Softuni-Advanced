import os

root_dir = os.path.dirname(os.path.abspath(__file__))
print(root_dir) #-> Check for root path

file_path = os.path.join(root_dir, "test_file.txt")
print(file_path) #-> Check for file path

if os.path.isfile(file_path):
    print("Found file!")
    
    with open(file_path, "r") as file:
        
        #data = file.readlines()
        #print([el for el in data], end="")
        
        for line in file:
            print(line, end="")
            
    
else:
    print("File not found error!")