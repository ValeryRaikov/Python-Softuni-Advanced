n = int(input())

res_list = set()

for _ in range(n):
    res_code = input()
    
    res_list.add(res_code)
    
while True:
    guest = input()
    
    if guest == "END":
        break
    
    if guest in res_list:
        res_list.remove(guest)
        
print(len(res_list))
[print(guest) for guest in (sorted(res_list))]