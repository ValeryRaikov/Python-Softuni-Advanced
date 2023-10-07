from functools import reduce
from math import floor

expression = input().split()

functions = {
    "+": lambda i: reduce(lambda x, y: x + y, map(int, expression[:i])),
    "-": lambda i: reduce(lambda x, y: x - y, map(int, expression[:i])),
    "*": lambda i: reduce(lambda x, y: x * y, map(int, expression[:i])),
    "/": lambda i: reduce(lambda x, y: x / y, map(int, expression[:i])),
}

idx = 0
while len(expression) > idx:
    symbol = expression[idx]
    
    if symbol in "+-*/":
        expression[0] = functions[symbol](idx)
        [expression.pop(1) for i in range(idx)]
        idx = 1
        
    idx += 1
        
print(floor(int(expression[0])))