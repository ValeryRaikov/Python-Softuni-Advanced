SIZE = 6

mars_field = []
rover_position = []

directions = {
    "up": lambda r, c: [(r - 1) % SIZE, c],
    "down": lambda r, c: [(r + 1) % SIZE, c],
    "left": lambda r, c: [r, (c - 1) % SIZE],
    "right": lambda r, c: [r, (c + 1) % SIZE],
}

deposits = {
    "W": ["Water", 0],
    "M": ["Metal", 0],
    "C": ["Concrete", 0],
}

for row in range(SIZE):
    current_row = input().split()
    mars_field.append(current_row)
    
    if "E" in current_row:
        rover_position = [row, mars_field[row].index("E")]
        
commands = input().split(", ")

for command in commands:
    rover_position = directions[command](rover_position[0], rover_position[1])
    curr_position = mars_field[rover_position[0]][rover_position[1]]
    
    if curr_position == "R":
        print(f"Rover got broken at {(rover_position[0], rover_position[1])}")
        break
    elif curr_position == "-":
        continue
    else:
        deposits[curr_position][1] += 1
        print(f"{deposits[curr_position][0]} deposit found at {(rover_position[0], rover_position[1])}")

deposits_counter = 0
for values in deposits.values():
    if values[1] >= 1:
        deposits_counter += 1

if deposits_counter == 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")