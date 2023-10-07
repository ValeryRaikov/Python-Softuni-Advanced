class ValueCannotBeNegative(Exception):
    pass

for _ in range(5):
    try:
        number = int(input())
        
        if number < 0:
            raise ValueCannotBeNegative
    
    except ValueCannotBeNegative as e:
        print("Number must be positive!")