rows = int(input())
cols = rows

matrix = []
for _ in range(rows):
    matrix.append(list(input()))
    
searched_symbol = input()
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == searched_symbol:
            position = (i, j)
            print(position)
            exit(0)
            
print(f"{searched_symbol} does not occur in the matrix")

#########################################################

def search_symbol(matrix, symbol):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == symbol:
                return (i, j)
    
    return f"{symbol} does not occur in the matrix"

rows = int(input())

matrix = []
for _ in range(rows):
    matrix.append(list(input()))
   
searched_symbol = input()
 
print(search_symbol(matrix, searched_symbol))