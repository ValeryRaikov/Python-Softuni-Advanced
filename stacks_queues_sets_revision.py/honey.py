from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

functions = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y, 
    "*": lambda x, y: x * y, 
    "/": lambda x, y: x / y, 
}

total_honey = 0

while bees and nectar:
    curr_bee = bees.popleft()
    curr_nectar = nectar.pop()
    
    if curr_nectar < curr_bee:
        bees.appendleft(curr_bee)
    elif curr_nectar >= curr_bee:
        curr_symbol = symbols.popleft()
        
        if curr_symbol == "/" and curr_nectar == 0:
            continue
        else:
            total_honey += abs(functions[curr_symbol](curr_bee, curr_nectar))
        
print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
    
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")