rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

diagonal_sum = 0
for i in range(rows):
    diagonal_sum += matrix[i][i]
    
print(diagonal_sum)