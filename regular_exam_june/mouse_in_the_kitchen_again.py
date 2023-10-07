def check_is_valid_index(row, col):
    return 0 <= row < N and 0 <= col < M

N, M = [int(x) for x in input().split(",")]

cheese_count = 0

cupboard = []
mouse_position = []
for row in range(N):
    current_row = list(input())
    cupboard.append(current_row)
    
    if "M" in current_row:
        mouse_position = [row, cupboard[row].index("M")]
        
    if "C" in current_row:
        cheese_count += cupboard[row].count("C")
    
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}    

old_mouse_position = mouse_position.copy()

command = input()
while command != "danger":
    mouse_position_row = mouse_position[0] + directions[command][0]
    mouse_position_col = mouse_position[1] + directions[command][1]
    if check_is_valid_index(mouse_position_row, mouse_position_col):
        mouse_position = [mouse_position_row, mouse_position_col]
        
        if cupboard[mouse_position_row][mouse_position_col] == "C":
            cheese_count -= 1
            if not cheese_count:
                cupboard[mouse_position_row][mouse_position_col] = "M"
                print("Happy mouse! All the cheese is eaten, good night!")
                [print(*row, sep="") for row in cupboard]
                break
            else:
                cupboard[mouse_position_row][mouse_position_col] = "*"
                
        elif cupboard[mouse_position_row][mouse_position_col] == "@":
            cupboard[old_mouse_position[0]][old_mouse_position[1]] = "M"
            command = input()
            continue
        
        elif cupboard[mouse_position_row][mouse_position_col] == "T":
            print("Mouse is trapped!")
            cupboard[mouse_position_row][mouse_position_col] = "M"
            [print(*row, sep="") for row in cupboard]
            break
    
    else:
        cupboard[mouse_position[0]][mouse_position[1]] = "M"
        print("No more cheese for tonight!")
        [print(*row, sep="") for row in cupboard]
        break
    
    old_mouse_position = mouse_position
    command = input() 
    
#[print(*row, sep="") for row in cupboard]