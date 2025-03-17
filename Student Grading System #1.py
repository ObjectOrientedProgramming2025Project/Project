import csv

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

class Student_Grading_System:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self):
        student_id = input("Enter Your Students ID: ")
        if student_id in self.students:
            print("Student is already made")
            return

        name = input("Enter the students name: ")
        self.students[student_id] = Student(student_id, name)

    def menu(self):
        while True:
            print("Student Grading System:")
            print("1. Add Student")
            print("2. Exit")
            choice = input("Enter your Choice: ")
            if choice == "1":
                self.add_student()

            elif choice == "2":
                break

            else:
                print("Invalid input, please try again")

if __name__ == "__main__":
    system = Student_Grading_System()
    system.menu()
