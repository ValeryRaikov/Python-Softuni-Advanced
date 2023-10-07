from collections import deque

def check_is_valid_indices(row, col):
    return 0 <= row < rows and 0 <= col < cols

rows = cols = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

bombs_coordinates = deque(input().split())

positions = (
    (-1, -1), #up_left_diagonal
    (-1, 0), #up
    (-1, 1), #up_right_diagonal
    (0, -1), #left
    (0, 1), #right
    (1, -1), #down_left_diagonal
    (1, 0), #down
    (1, 1), #down_right_diagonal
)

for _ in range(len(bombs_coordinates)):
    curr_bomb = bombs_coordinates.popleft()
    curr_bomb_row, curr_bomb_col = [int(x) for x in curr_bomb.split(",")]

    bomb_power = matrix[curr_bomb_row][curr_bomb_col]
    
    for pos in positions:
        new_row = curr_bomb_row + pos[0]
        new_col = curr_bomb_col + pos[1]
        if check_is_valid_indices(new_row, new_col):
            if matrix[new_row][new_col] > 0:
                matrix[new_row][new_col] -= bomb_power
            
            matrix[curr_bomb_row][curr_bomb_col] = 0
         
alive_cels_counter = 0    
alive_cels_sum = 0   
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > 0:
            alive_cels_counter += 1
            alive_cels_sum += matrix[i][j]

print(f"Alive cells: {alive_cels_counter}")
print(f"Sum: {alive_cels_sum}")
[print(*row) for row in matrix]