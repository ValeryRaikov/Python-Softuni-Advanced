def check_is_valid(row, col):
    return 0 <= row < size and 0 <= col < size

size = int(input())

field = []

bunny_pos = []
winning_path = []
best_direction = None

max_sum_eggs = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0), 
    "left": (0, -1), 
    "right": (0, 1), 
}

for row in range(size):
    field.append(input().split())
    
    if "B" in field[row]:
        bunny_pos = [row, field[row].index("B")]
        
for direction, position in directions.items():
    row, col = [bunny_pos[0] + position[0], bunny_pos[1] + position[1]]
    
    path = []
    total_sum_eggs = 0
    
    while check_is_valid(row, col):
        if field[row][col] == "X":
            break
        
        total_sum_eggs += int(field[row][col])
        path.append([row, col])
        
        row += position[0]
        col += position[1]
        
        if total_sum_eggs >= max_sum_eggs:
            max_sum_eggs = total_sum_eggs
            best_direction = direction
            winning_path = path

print(best_direction)
print(*winning_path, sep="\n")
print(max_sum_eggs)