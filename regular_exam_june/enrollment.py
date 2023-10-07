def gather_credits(credits, *args):
    courses = []
    
    total_credits = 0
    for info in args:
        if info[0] not in courses:
            if total_credits < credits:
                courses.append(info[0])
                total_credits += info[1]
            else:
                break
                
    if total_credits >= credits:
        return f"Enrollment finished! Maximum credits: {total_credits}.\nCourses: {', '.join(sorted(courses))}"
                
    return f"You need to enroll in more courses! You have to gather {credits - total_credits} credits more."       

  
print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 30),
    ("Fundamentals", 19),
))