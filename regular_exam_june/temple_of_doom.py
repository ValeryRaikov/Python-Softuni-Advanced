from collections import deque

tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])
challenges = [int(x) for x in input().split()]

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()
    multiplication_result = tool * substance

    if multiplication_result in challenges:
        challenges.remove(multiplication_result)
    else:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance <= 0:
            continue
        
        substances.append(substance)
        
if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
    
if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")