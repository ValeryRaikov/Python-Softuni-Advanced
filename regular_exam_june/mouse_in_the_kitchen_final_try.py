def check_is_valid_index(row, col):
    return 0 <= row < N and 0 <= col < M

N, M = [int(x) for x in input().split(",")]

cheese_count = 0

cupboard = []
mouse_position = []
for r in range(N):
    current_row = list(input())
    cupboard.append(current_row)
    
    if "M" in current_row:
        mouse_position = [r, cupboard[r].index("M")]
        
    if "C" in current_row:
        cheese_count += cupboard[r].count("C")
    
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}   

command = input()
while command != "danger":
    r = mouse_position[0] + directions[command][0]
    c = mouse_position[1] + directions[command][1]
    if check_is_valid_index(r, c):
        if cupboard[r][c] == "@":
            command = input()
            continue
        else:
            cupboard[mouse_position[0]][mouse_position[1]] = "*"
            if cupboard[r][c] == "C":
                cheese_count -= 1
                if not cheese_count:
                    cupboard[r][c] = "M"
                    print("Happy mouse! All the cheese is eaten, good night!")
                    [print(*row, sep="") for row in cupboard]
                    break
                else:
                    cupboard[r][c] = "*"
            elif cupboard[r][c] == "T":
                print("Mouse is trapped!")
                cupboard[r][c] = "M"
                [print(*row, sep="") for row in cupboard]
                break     
    else: 
        cupboard[r][c] = "M"
        print("No more cheese for tonight!")
        [print(*row, sep="") for row in cupboard]
        break
    
    mouse_position = [mouse_position[0] + directions[command][0], mouse_position[1] + directions[command][1]]
    
    command = input()