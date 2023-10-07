def check_is_valid_index(row, col):
    return 0 <= row < SIZE and 0 <= col < SIZE

PRESENTS = int(input())
presents_copy = PRESENTS
SIZE = int(input())

positions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

neighborhood = []
santas_pos = []
for row in range(SIZE):
    current_row = input().split()
    neighborhood.append(current_row)
    
    if "S" in current_row:
        santas_pos = [row, neighborhood[row].index("S")]
        
command = input()
while presents_copy > 0 and command != "Christmas morning":
    new_santas_pos = [santas_pos[0] + positions[command][0], santas_pos[1] + positions[command][1]]
    neighborhood[santas_pos[0]][santas_pos[1]] = "-"
    
    if neighborhood[new_santas_pos[0]][new_santas_pos[1]] == "C":
        for pos in positions:
            if neighborhood[new_santas_pos[0] + positions[pos][0]][neighborhood[new_santas_pos[1] + positions[pos][1]]] == "X":
                presents_copy -= 0
                neighborhood[new_santas_pos[0] + positions[pos][0]][neighborhood[new_santas_pos[1] + positions[pos][1]]] = "-"
    elif neighborhood[new_santas_pos[0]][new_santas_pos[1]] == "V":
        presents_copy -= 1
        neighborhood[new_santas_pos[0]][new_santas_pos[1]] = "-"
        
    santas_pos = new_santas_pos
    
    command = input()
    
[print(*row) for row in neighborhood]

for row in neighborhood:
    if "V" in row:
        print("Santa ran out of presents!")
        break
else:
    print(f"Good job, Santa! {PRESENTS - presents_copy} happy nice kid/s.")