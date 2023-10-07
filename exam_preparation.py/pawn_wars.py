def find_pawn_position(search_for, pawn_position, r):
    if search_for in board[r]:
        pawn_position.append(r)
        pawn_position.append(board[r].index(search_for))
        return pawn_position

SIZE = 8

board = []
white_pawn_coordinates = []
black_pawn_coordinates = []

for row in range(SIZE):
    board.append(input().split())
    
    find_pawn_position("w", white_pawn_coordinates, row)
    find_pawn_position("b", black_pawn_coordinates, row)
    
white_pawn_transposed = [SIZE - white_pawn_coordinates[0] - 1, white_pawn_coordinates[1]]
    
if abs(white_pawn_coordinates[1] - black_pawn_coordinates[1]) != 1:
    if SIZE - white_pawn_transposed[0] <= SIZE - black_pawn_coordinates[0]:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + white_pawn_coordinates[1])}8.")
    else:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + black_pawn_coordinates[1])}1.")
else:
    if abs(white_pawn_coordinates[0] - black_pawn_coordinates[0]) % 2 != 0:
        kill_square = [chr(97 + black_pawn_coordinates[1]), ((SIZE - white_pawn_coordinates[0] + SIZE - black_pawn_coordinates[0]) + 1) // 2]
        print(f"Game over! White win, capture on {''.join([str(x) for x in kill_square])}.")
    else:
        kill_square = [chr(97 + white_pawn_coordinates[1]), (SIZE - white_pawn_coordinates[0] + SIZE - black_pawn_coordinates[0]) // 2]
        print(f"Game over! Black win, capture on {''.join([str(x) for x in kill_square])}.")