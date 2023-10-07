from collections import deque

queue = deque(input().split())
kill_toss = int(input())

while len(queue) > 1:
    queue.rotate(-kill_toss)
    print(f"Removed {queue.pop()}")
    
print(f"Last is {queue.pop()}")
