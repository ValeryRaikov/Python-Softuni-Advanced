text = input()

try:
    times = int(input())
    print(text * times)
    
except ValueError as e:
    print("Variable times must be an integer")