numbers = tuple([float(x) for x in input().split()])

numbers_freq = {}

for number in numbers:
    if number not in numbers_freq:
        numbers_freq[number] = 1
    else:
        numbers_freq[number] += 1
        
for number, freq in numbers_freq.items():
    print(f"{number:.1f} - {freq} times")
    
#################################################

numbers = tuple([float(x) for x in input().split()])

numbers_freq = {}

for number in numbers:
    numbers_freq[number] = numbers.count(number)

for number, freq in numbers_freq.items():
    print(f"{number:.1f} - {freq} times")