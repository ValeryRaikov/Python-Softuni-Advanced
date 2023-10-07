rows = int(input())

matrix = []
for _ in range(rows):
    matrix.extend([int(x) for x in input().split(", ")])
    
print(matrix)

#######################################################

rows = int(input())

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
    
flattened = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        flattened.append(matrix[i][j])
        
print(flattened)