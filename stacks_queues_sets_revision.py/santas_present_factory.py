from collections import deque

materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

presents_table = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

crafted_presents = []

while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[0] else 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0
    
    if not magic_level:
        continue
    
    product = material * magic_level
    
    if presents_table.get(product):
        crafted_presents.append(presents_table[product])
    elif product < 0:
        materials.append(material + magic_level)
    elif product > 0:
        materials.append(material + 15)
        

subset_1 = {"Doll", "Wooden train"}
subset_2 = {"Teddy bear", "Bicycle"}
    
if subset_1.issubset(crafted_presents) or subset_2.issubset(crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
    
if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")
    
[print(f"{toy}: {crafted_presents.count(toy)}") for toy in sorted(set(crafted_presents))]