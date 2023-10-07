from collections import deque

text = deque([int(x) for x in input().split()])

while len(text):
    print(text.pop(), end=" ")
    
########################################################

text = deque(map(int, input().split()))

for _ in range(len(text)):
    print(text.pop(), end=" ")
    
########################################################

text = list(map(int, input().split()))
queue = deque()

for _ in range(len(text)):
    queue.append(str(text.pop()))
    
print(" ".join(queue))