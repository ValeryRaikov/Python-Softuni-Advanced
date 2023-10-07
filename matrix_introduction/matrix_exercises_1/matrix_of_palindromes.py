rows, cols = [int(x) for x in input().split()]

start = ord('a')
for i in range(start, start + rows):
    for j in range(start,  start + cols):
        print(f"{chr(i)}{chr(i + j - start)}{chr(i)}", end=" ")
        
    print()
    
############################################################

rows, cols = [int(x) for x in input().split()]

start = ord('a')
for i in range(start, start + rows):
    for j in range(i, i + cols):
        print(f"{chr(i)}{chr(j)}{chr(i)}", end=" ")
        
    print()