#generator

"""test_nums = ['1', '2', '3', '4', '5']
this_gen = (int(el) for el in test_nums)

print(type(this_gen))
print(tuple(this_gen))

matrix = [
    [1,2,3,],
    [4,5,6,],
    [7,8,9,],
]

matrix.reverse()
[print(*row) for row in matrix]
print(*matrix, sep='\n')

def test_func(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
        
    return total_sum

numbers = list(range(10))
result = test_func(numbers)
print(f"Result: {result}")

email = "valeryraikov@gmail.com"
first, second = email.split("@")
second, third = second.split(".")
print(first, second, third)

deposits = {
    "W": ["Water", 1],
    "M": ["Metal", 3],
    "C": ["Concrete", 0],
}
this_set = set()
for item in deposits.values():
    if item[1] >= 1:
        this_set.add(item[0])
        
if len(this_set) == 3:
    print("Yes")
else:
    print("No")"""
