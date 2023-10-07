"""def check_is_valid(row, col):
    return 0 <= row < rows and 0 <= col < rows

rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input()
while command != "END":
    operation, *data = command.split()
    row, col, value = [int(x) for x in data]
    
    if check_is_valid(row, col):
        if operation == "Add":
            matrix[row][col] += value
        else:
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    
    command = input()
    
[print(*row) for row in matrix]"""

################################################

def check_is_valid(row, col):
    return 0 <= row < rows and 0 <= col < rows

rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

functions = {
    "Add": lambda x: matrix[row][col] + x,
    "Subtract": lambda x: matrix[row][col] - x,
}

command = input().split()
while command[0] != "END":
    operation, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])
    
    if check_is_valid(row, col):
        matrix[row][col] = functions[operation](value)
    else:
        print("Invalid coordinates")
    
    command = input().split()
    
[print(*row) for row in matrix]