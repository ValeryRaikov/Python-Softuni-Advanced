""" names = set()

for _ in range(int(input())):
    names.add(input())
    
print(*names, sep='\n') """

#################################

print(*{input() for _ in range(int(input()))}, sep='\n')