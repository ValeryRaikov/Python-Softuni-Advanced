import os

root_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_dir, "numbers.txt")

numbers = []
total_sum = 0
try:
    with open(file_path, "r") as file:
        numbers = file.readlines()
        for num in numbers:
            total_sum += int(num)
except FileNotFoundError:
    print("File not found!")
else:   
    print(f"The sum is {total_sum}")