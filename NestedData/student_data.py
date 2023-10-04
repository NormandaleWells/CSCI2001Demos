import json


def main():
    f = open('student_data.json', 'r')
    json_data = f.read()
    f.close()

    student_data = json.loads(json_data)
    print(student_data)

if __name__ == "__main__":
    main()
