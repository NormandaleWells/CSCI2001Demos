'''
Program to read student_data.txt, and produce student_data.json.
'''

import json

student_data = {}

f = open('student_data.txt', 'r')
for line in f:
    line = line.strip()
    fields = line.split()
    for i in range(3, len(fields)):
        fields[i] = int(fields[i])

    this_student = {}

    id = fields[0]
    name = (fields[1], fields[2])
    this_student['name'] = name

    scores = {}
    scores['assignments'] = fields[3:7]
    scores['exams'] = fields[7:9]
    this_student['scores'] = scores

    student_data[id] = this_student

f.close()

f = open("student_data.json", 'w')
f.write(json.dumps(student_data, indent=2))
f.close()
