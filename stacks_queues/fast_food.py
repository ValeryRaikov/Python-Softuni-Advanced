from collections import deque

total_food = int(input())

queue = deque([int(x) for x in input().split()])

print(max(queue))

for order in queue.copy():
    if order <= total_food:
        queue.popleft()
        total_food -= order
    else:
        print(f"Orders left: {' '.join([str(x) for x in queue])}")
        break
else:
    print("Orders complete")