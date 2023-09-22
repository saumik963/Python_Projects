from School_User import School, ClaasRoom, Subject
from School_persons import Student, Teacher


def main():
    school = School("Liberty School", "Dhaka")

    eight = ClaasRoom("eight")
    school.add_classroom(eight)
    nine = ClaasRoom("nine")
    school.add_classroom(nine)
    ten = ClaasRoom("ten")
    school.add_classroom(ten)

    jhon = Student("Jhon Wick", eight)
    school.student_admission(jhon)
    nobody = Student("Nobody", eight)
    school.student_admission(nobody)
    jems = Student("Jems Bond", eight)
    school.student_admission(jems)

    physics_teacher = Teacher("Bruch Baner")
    physics = Subject("Physics", physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher("Nick Furry")
    chemistry = Subject("Chemistry", chemistry_teacher)
    eight.add_subject(chemistry)

    biology_teacher = Teacher("Peter Parker")
    biology = Subject("Biology", biology_teacher)
    eight.add_subject(biology)


    eight.take_semister_final()

    print(school)


if __name__ == "__main__":
    main()
