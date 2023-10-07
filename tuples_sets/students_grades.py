n = int(input())

students_grades = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)
    
    if name not in students_grades:
        students_grades[name] = []
        
    students_grades[name].append(grade)
        
for name, grades in students_grades.items():
    avg_res = sum(grades)/len(grades)
    print(f"{name} -> {' '.join([str(f'{grade:.2f}') for grade in grades])} (avg: {avg_res:.2f})")
    
################################################################################################

n = int(input())

students_grades = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)
    
    students_grades[name] = students_grades.get(name, [])
    students_grades[name].append(grade)
        
for name, grades in students_grades.items():
    avg_res = sum(grades)/len(grades)
    print(f"{name} -> {' '.join([str(f'{grade:.2f}') for grade in grades])} (avg: {avg_res:.2f})")