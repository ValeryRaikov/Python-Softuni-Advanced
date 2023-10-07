from collections import deque

def fill_the_box(height, length, width, *cubes):
    box_size = height * length * width
    cubes = deque(cubes)
    
    while cubes[0] != "Finish":
        box_size -= cubes.popleft()
        
        if box_size < 0:
            cubes_left = sum(x for x in cubes if x != "Finish")
            return f"No more free space! You have {cubes_left + abs(box_size)} more cubes."
    
    return f"There is free space in the box. You could put {box_size} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))      
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))