from collections import deque

clothes = deque([int(x) for x in input().split()])

rack_capacity = int(input())

rack_count = 1   

current_capacity = rack_capacity
while len(clothes):
    cloth = clothes.pop()
    if current_capacity >= cloth:
        current_capacity -= cloth
    else:
        rack_count += 1
        current_capacity = rack_capacity - cloth

print(rack_count)