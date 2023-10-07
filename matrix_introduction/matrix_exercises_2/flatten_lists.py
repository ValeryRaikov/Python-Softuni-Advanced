input_line = input().split("|")

flattened = []
for substring in reversed(input_line):
    flattened.extend(substring.split())
    
print(*flattened)

##########################################################

#numbers = [substring.split() for substring in input().split("|")]
#print(*[" ".join(sublist) for sublist in reversed(numbers) if sublist])