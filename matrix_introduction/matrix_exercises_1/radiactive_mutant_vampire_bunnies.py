rows, cols = [int(x) for x in input().split()]

matrix = [list(input()) for _ in range(rows)]
moves = list(input())

wins = False
directions = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}

def find_player_position():
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "P":
                return i, j
            
def check_valid_index(row, col, player = False):
    global wins
    
    if 0 <= row < rows and 0 <= col < cols:
        return True
    if player:
        wins = True
        
def check_player_alive(row, col):
    if matrix[row][col] == "B":
        show_results("dead")
        
def bunnies_positions():
    positions = []
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "B":
                positions.append([i, j])
                
    return positions

def bunnies_move(bunnies_pos):
    for row, col in bunnies_pos:
        for bunnie_move in directions.values():
            new_row, new_col = row + bunnie_move[0] , col + bunnie_move[1]
            
            if check_valid_index(new_row, new_col):
                matrix[new_row][new_col] = "B"
                
def show_results(status = "won"):
    [print(*row, sep="") for row in matrix]
    print(f"{status}: {player_row} {player_col}")
    
    exit(0)


player_row, player_col = find_player_position()
matrix[player_row][player_col] = '.'

for move in moves:
    player_movement_row, player_movement_col = player_row + directions[move][0], player_col + directions[move][1]
    
    if check_valid_index(player_movement_row, player_movement_col, True):
        player_row, player_col = player_movement_row, player_movement_col
        
    bunnies_move(bunnies_positions())
    
    if wins:
        show_results()
        
    check_player_alive(player_row, player_col)