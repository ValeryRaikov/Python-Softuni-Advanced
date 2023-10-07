numbers = [int(x) for x in input().split()]

target_number = int(input())

for i in range(len(numbers)):
    if numbers[i] == "":
        continue
    for j in range(i + 1, len(numbers)):
        if numbers[j] == "":
            continue
        
        if numbers[i] + numbers[j] == target_number:
            print(f"{numbers[i]} + {numbers[j]} = {target_number}")
            numbers[i] = ""
            numbers[j] = ""
            break