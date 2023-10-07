n = int(input())

cars = set()

for _ in range(n):
    direction, registration = input().split(", ")
    
    if direction == "IN":
        cars.add(registration)
    else:
        cars.remove(registration)
        
if cars:
    print(*cars, sep = '\n')
else:
    print("Parking Lot is Empty")