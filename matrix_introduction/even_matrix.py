rows = int(input())

matrix = []
for _ in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    matrix.append([num for num in inner_list if num % 2 == 0])
    
print(matrix)

#########################################################

rows = int(input())
matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(rows)]
      
print(matrix)