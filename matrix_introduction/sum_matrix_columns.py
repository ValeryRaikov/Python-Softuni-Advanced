#rows, cols = [int(x) for x in input().split(", ")]
rows, cols = map(int, input().split(", "))

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for j in range(cols):
    current_sum = 0
    for i in range(rows):
        current_sum += matrix[i][j]
        
    print(current_sum)