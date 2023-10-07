rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

def check_indices_validity(indices):
    row1, col1, row2, col2 = indices
    return 0 <= row1 < rows and 0 <= row2 < rows and 0 <= col1 < cols and 0 <= col2 < cols
        
def swap_positions(command, indices):
    if command == "swap" and len(indices) == 4 and check_indices_validity(indices):
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")
         

command = input()
while command != "END":
    cmd_type, *data = [int(x) if x.isdigit() else x for x in command.split()]
    
    swap_positions(cmd_type, data)
    
    command = input()