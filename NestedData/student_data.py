import json


def main():
    f = open('student_data.json', 'r')
    json_data = f.read()
    f.close()

    students = json.loads(json_data)
    #print(json.dumps(students, indent=2))
    for id,student_data in students.items():
        assert 'name' in student_data
        first_name = student_data['name'][0]
        last_name = student_data['name'][1]
        assert 'scores' in student_data
        assignments = student_data['scores']['assignments']
        exams = student_data['scores']['exams']
        asgn_avg = sum(assignments) / len(assignments)
        exams_avg = sum(exams) / len(exams)
        print(f'{id} {first_name} {last_name} {asgn_avg} {exams_avg}')

    # for id in students:
    #     print(id)
    # id = input("Select a student: ")
    # assert id in students
    # print(students[id])


if __name__ == "__main__":
    main()
