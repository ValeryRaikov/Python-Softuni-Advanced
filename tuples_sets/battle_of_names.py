odd_set = set()
even_set = set()

for i in range(1, int(input()) + 1):
    ascii_sum = sum(ord(letter) for letter in input())//i
    
    odd_set.add(ascii_sum) if ascii_sum % 2 != 0 else even_set.add(ascii_sum)
    
if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')