import os

root_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_dir, "even_lines.txt")

SPECIAL_SYMBOLS = ["-", ",", ".", "!", "?"]

if os.path.isfile(file_path):
    with open(file_path, "r") as file:

        even_lines = []
        lines_counter = 0
        for line in file.readlines():
            if lines_counter % 2 == 0:
                even_lines.append(line.rstrip('\n'))

            lines_counter += 1
            
    replaced_lines = []
    for line in even_lines:
        for symbol in SPECIAL_SYMBOLS:
            if symbol in line:
                line = line.replace(symbol, '@')
                
        replaced_lines.append(line)
    
    reversed_line = []            
    for line in replaced_lines:
        line = line.split()[::-1]
        for word in line:
            reversed_line.append(word)
            
        print(" ".join(reversed_line))
        
        reversed_line = []
else:
    print("File not found!")