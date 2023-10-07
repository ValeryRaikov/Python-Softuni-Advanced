from collections import deque

text = input()
stack = deque(text)

while stack:
    print(stack.pop(), end="")

######################################################

from collections import deque

text = list(input())
stack = deque()

for i in range(len(text)):
    stack.append(text.pop())
    
print("".join(stack))