rows, cols = [int(x) for x in input().split(", ")]

matrix = []
total_sum = 0
for i in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    total_sum += sum(inner_list)
    
    matrix.append(inner_list)
    
print(total_sum)
print(matrix)

##########################################################

rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

total_sum = 0
for i in range(rows):
    for j in range(cols):
        total_sum += matrix[i][j]

print(total_sum)
print(matrix)