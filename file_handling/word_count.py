import os
import re
from collections import defaultdict

root_dir = os.path.dirname(os.path.abspath(__file__))

words_file_path = os.path.join(root_dir, "words.txt")

words = []
try:
    with open(words_file_path, "r") as file:
        words = file.readline().split()
except FileNotFoundError:
    print("File not found!")
    
input_text_file_path = os.path.join(root_dir, "input.txt")

input_text = []
try:
    with open(input_text_file_path, "r") as file:
        input_text = file.readlines()
except FileNotFoundError:
    print("File not found!")
    
re_pattern = r"[^\w\s]"
clear_text = []
for line in input_text:
    clear_text.append(re.sub(re_pattern, "", line.lower().rstrip('\n')))

matches = defaultdict(lambda: 0)
for word in words:
    for line in clear_text:
        if word in line:
            matches[word] += 1
            
for word, occ in sorted(matches.items(), key=lambda x: -x[1]):
    print(f"{word} - {occ}")