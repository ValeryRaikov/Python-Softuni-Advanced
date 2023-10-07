from collections import deque

GREEN_LIGHT_DURATION = int(input())
free_window_duration = int(input())

cars = deque()
passed_cars = 0

command = input()
while command != "END":
    if command != "green":
        cars.append(command)
    elif command == "green":
        green_light_duration_copy = GREEN_LIGHT_DURATION
        while cars:
            current_car = cars.popleft()
            if green_light_duration_copy > 0:
                if len(current_car) < green_light_duration_copy:
                    green_light_duration_copy -= len(current_car)
                    passed_cars += 1
                else:
                    car_stuck = len(current_car) - green_light_duration_copy
                    if free_window_duration < car_stuck:
                        print("A crash happened!")
                        print(f"{current_car} was hit at {abs(free_window_duration - car_stuck)}.")
                        break
                    else:
                        green_light_duration_copy = GREEN_LIGHT_DURATION
                        passed_cars += 1

    command = input()

else:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
