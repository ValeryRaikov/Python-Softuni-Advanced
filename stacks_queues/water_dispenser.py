from collections import deque

queue = deque()

litters = int(input())
name = input()
while name != "Start":
    queue.append(name)
    name = input()
    
command = input()
while command != "End":
    command_args = command.split()
    if len(command_args) == 1:
        litters_to_drink = int(command_args[0])
        if litters >= litters_to_drink:
            litters -= litters_to_drink
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
    else:
        litters_to_refil = int(command_args[1])
        litters += litters_to_refil
        
    command = input()
    
print(f"{litters} liters left")