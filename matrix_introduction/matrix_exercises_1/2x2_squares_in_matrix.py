rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

sub_matrix_counter = 0
for i in range(rows - 1):
    for j in range(cols - 1):
        curr_el = matrix[i][j]
        next_el = matrix[i][j+1]
        below_el = matrix[i+1][j]
        diagonal_el = matrix[i+1][j+1]
        
        if curr_el == next_el and curr_el == below_el and curr_el == diagonal_el:
            sub_matrix_counter += 1
            
print(sub_matrix_counter)