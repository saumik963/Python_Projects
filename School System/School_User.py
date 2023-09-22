class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teachers(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        className = student.classroom.name
        if className in self.classrooms:
            # TODO: add student id,roll
            self.classrooms[className].add_student(student)
        else:
            print(f"No classroom ad named {className}")

    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return 'A+'
        elif 70 <= marks < 80:
            return 'A'
        elif 60 <= marks < 70:
            return 'A-'
        elif 50 <= marks < 60:
            return 'B'
        elif 40 <= marks < 50:
            return 'C'
        elif 33 <= marks < 40:
            return 'D'
        else:
            return "F"

    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00,
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'C': 2.00,
            'D': 1.00,
            'F': 0.00
        }
        return grade_map[grade]

    @staticmethod
    def value_to_grade(value):
        if 4.5 <= value <= 5.00:
            return 'A+'
        elif 3.5 <= value < 4.5:
            return 'A'
        elif 3.0 <= value < 3.5:
            return 'A-'
        elif 2.5 <= value < 3.0:
            return 'B'
        elif 2.0 <= value < 2.5:
            return 'C'
        elif 1.0 <= value < 2.0:
            return 'D'
        else:
            return "F"
            

    def __repr__(self):
        print("__________All ClassRooms_______")
        for key, value in self.classrooms.items():
            print(key)

        print("______Students_______")
        eight = self.classrooms['eight']
        print(len(eight.students))
        for student in eight.students:
            print(student.name)

        print("_____Subjects_____")
        for subject in eight.subjects:
            print(f"{subject.name}  {subject.teacher.name}")

        print("________Students Exam Marks_______")
        for student in eight.students:
            for key, value in student.marks.items():
                print(student.name, key, "Marks:",
                      value, student.subject_grade[key])

            print("______End______")

        return ''


class ClaasRoom:
    def __init__(self, name):
        self.name = name
        # compisition
        self.students = []
        self.subjects = []

    def add_student(self, student):
        serial_id = f"{self.name}-{len(self.students)+1}"
        student.id = serial_id
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def __str__(self):
        return f'{self.name}-{len(self.students)}'

    # TODO: sort student by grade
    def get_top_students(self):
        pass

    def take_semister_final(self):
        # take exam
        for subject in self.subjects:
            subject.exam(self.students)

        # calculate final grade
        for student in self.students:
            student.calculate_final_grade()


class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 30

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark)
