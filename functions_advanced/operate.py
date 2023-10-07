from functools import reduce

def operate(operation, *args):
    if operation == "+":
        return reduce(lambda x, y: x + y, args)
    elif operation == "-":
        return reduce(lambda x, y: x - y, args)
    elif operation == "*":
        return reduce(lambda x, y: x * y, args)
    elif operation == "/":
        return reduce(lambda x, y: x / y, args)
    
print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

#####################################################

def operate(operation, *args):
    return reduce(lambda x, y: eval(f"{x}{operation}{y}"), args)

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))