first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [first.add(el) for el in x],
    "Add Second" : lambda x: [second.add(el) for el in x],
    "Remove First": lambda x: [first.discard(el) for el in x],
    "Remove Second": lambda x: [second.discard(el) for el in x],
    "Check Subset": lambda x: print(first.issubset(second) or second.issubset(first)),
}

for _ in range(int(input())):
    first_cmd, second_cmd, *data = input().split()
    
    result_cmd = first_cmd + " " + second_cmd
    
    functions[result_cmd]([int(x) for x in data])
    
print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")