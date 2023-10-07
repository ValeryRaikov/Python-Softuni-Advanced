def check_is_valid(row, col):
    return 0 <= row < size and 0 <= col < size

size = int(input())

board = [list(input()) for _ in range(size)]

positions = (
    (-2, -1), 
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, -1),
    (2, 1),
    (1, -2),
    (1, 2),
)

removed_knigths = 0
while True:
    max_attacks = 0
    knight_with_most_attack_pos = []
    
    for i in range(size):
        for j in range(size):
            if board[i][j] == "K":
                attacks = 0
                for pos in positions:
                    row_to_move = i + pos[0]
                    col_to_move = j + pos[1]
                    
                    if check_is_valid(row_to_move, col_to_move):
                        if board[row_to_move][col_to_move] == "K":
                            attacks += 1
                            
                if attacks > max_attacks:
                    knight_with_most_attack_pos = [i, j]
                    max_attacks = attacks
                    
    if knight_with_most_attack_pos:
        r, c = knight_with_most_attack_pos
        board[r][c] = "0"
        removed_knigths += 1
    else:
        break
                            
print(removed_knigths)