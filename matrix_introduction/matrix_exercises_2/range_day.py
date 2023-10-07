def check_is_valid(row, col):
    return 0 <= row < SIZE and 0 <= col < SIZE

SIZE = 5

field = []
player_pos = []
shot_targets_pos = []
count_shot_targets = 0

for row in range(SIZE):
    field.append(input().split())
    
    if "A" in field[row]:
        player_pos = [row, field[row].index("A")]

directions = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}

for _ in range(int(input())):
    command_args = input().split()
    action = command_args[0]
    direction = command_args[1]
    if action == "move":
        steps = int(command_args[2])
        pos_to_move = [player_pos[0] + directions[direction][0] * steps, player_pos[1] + directions[direction][1] * steps]
        
        if check_is_valid(pos_to_move[0], pos_to_move[1]):
            if pos_to_move != "x":
                pos_to_move = "A"
                player_pos = "."
                player_pos[0], player_pos[1] = pos_to_move[0], pos_to_move[1]
                
    elif action == "shoot":
        to_shoot = [player_pos[0] + directions[direction][0], player_pos[1] + directions[direction][1]]
        while check_is_valid(to_shoot[0], to_shoot[1]):
            if to_shoot == "x":
                shot_targets_pos.append([to_shoot[0], to_shoot[1]])
                to_shoot = "."
                count_shot_targets += 1
                break
            
            to_shoot[0] += directions[direction][0]
            to_shoot[1] += directions[direction][1]
            
total_targets = field.count("x")
if count_shot_targets == total_targets:
    print(f"Training completed! All {count_shot_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - count_shot_targets} targets left.")
    
[print(*row) for row in shot_targets_pos]