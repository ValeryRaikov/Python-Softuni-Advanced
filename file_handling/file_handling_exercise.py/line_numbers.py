import os

SYMBOLS = [".", ",", "!", "?", ":", ";", "-", "'"]

root_dir = os.path.dirname(os.path.abspath(__file__))
read_file_path = os.path.join(root_dir, "text.txt")
write_file_path = os.path.join(root_dir, "output.txt")

if os.path.exists(read_file_path):
    with open(read_file_path, "r") as file:
        content = file.readlines()
else:
    print("File not found!")
    
with open(write_file_path, "w") as file:
    iterations = 1
    for line in content:
        line = line.rstrip('\n')
        words_counter = 0
        symbols_counter = 0
        for i in range(len(line)):
            if ord(line[i]) > 64 and ord(line[i]) < 123:
                words_counter += 1
            elif line[i] in SYMBOLS:
                symbols_counter += 1
                
        file.write(f"Line {iterations}: {line} -> words:{words_counter}, symbols:{symbols_counter}\n")
        
        iterations += 1