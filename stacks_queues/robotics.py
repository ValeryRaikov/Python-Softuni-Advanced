from collections import deque
from datetime import datetime, timedelta

robots = {}

for robot in input().split(";"):
    name, time = robot.split("-")
    robots[name] = [int(time), 0]
        
start_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()

product = input()
while product != "End":
    products.append(product)
    
    product = input()
    
while products:
    start_time += timedelta(0, 1)
    
    product = products.popleft()
    
    free_robots = []
    
    for robot_name, value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1
        
        if value[1] == 0:
            free_robots.append([robot_name, value])
            
    if not free_robots:
        products.append(product)
        continue
    
    robot_n, data = free_robots[0]
    robots[robot_n][1] = data[0]
    
    print(f"{robot_n} - {product} [{start_time.strftime('%H:%M:%S')}]")