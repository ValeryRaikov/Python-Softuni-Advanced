from collections import deque

stacked_nums = deque()

map_funcs = {
    1: lambda x: stacked_nums.append(x[1]),
    2: lambda x: stacked_nums.pop() if stacked_nums else None,
    3: lambda x: print(max(stacked_nums)) if stacked_nums else None,
    4: lambda x: print(min(stacked_nums)) if stacked_nums else None
}

iterations = int(input())

for _ in range(iterations):
    command = [int(x) for x in input().split()]
    map_funcs[command[0]](command)
    
stacked_nums.reverse()
print(", ".join([str(x) for x in stacked_nums]))

####################################################################

stacked_nums = deque()

iterations = int(input())

for _ in range(iterations):
    command = [int(x) for x in input().split()]
    
    if command[0] == 1:
        stacked_nums.append(command[1])
    elif command[0] == 2:
        if stacked_nums:
            stacked_nums.pop()
    elif command[0] == 3:
        print(max(stacked_nums))
    else:
        print(min(stacked_nums))
    
"""stacked_nums.reverse()
print(*stacked_nums, sep = ", ")"""

"""for _ in range(len(stacked_nums)):
    print(stacked_nums.pop(), end=", ")"""