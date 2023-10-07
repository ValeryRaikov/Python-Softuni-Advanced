from collections import deque

queue = deque()

name = input()
while name != "End":
    if name == "Paid":
        while queue:
            print(queue.popleft())
    else:  
        queue.append(name)
    
    name = input()
    
print(f"{len(queue)} people remaining.")

################################################

from collections import deque

queue = deque()

while True:
    name = input()
    if name == "Paid":
        while len(queue):
            print(queue.popleft())
    elif name == "End":  
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(name)