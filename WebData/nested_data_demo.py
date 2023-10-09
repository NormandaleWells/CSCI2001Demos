students = [
    { "name": ("john", "doe"),
      "grades" : { "assignments" : [90, 89, 75, 89], "exams" : [100, 85] }},
    { "name" : ("jane", "doe"),
      "grades" : { "assignments" : [99, 75, 89, 95], "exams" : [95, 95]} }]

for student in students:
    name = student['name']
    print(f"name = {name[1]}, {name[0]}")
    grades = student['grades']
    for name,items in grades.items():
        print(f"{name}: {items}")
