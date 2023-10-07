rows, cols = map(int, input().split(", "))

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

max_sum = float('-inf')
for i in range(rows - 1):
    for j in range(cols - 1):
        current_el = matrix[i][j]
        next_el = matrix[i][j+1]
        below_el = matrix[i+1][j]
        diagonal_el = matrix[i+1][j+1]
        
        current_sum = current_el + next_el + below_el + diagonal_el
        
        if current_sum > max_sum:
            max_sum = current_sum
            
            sub_matrix = [[current_el, next_el], [below_el, diagonal_el]]
            
print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)