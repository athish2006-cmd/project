class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []
    def enroll(self, course):
        self.courses.append(course)
    def __str__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name})"
class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.courses = []
    def assign_course(self, course):
        self.courses.append(course)
    def __str__(self):
        return f"Teacher(ID: {self.teacher_id}, Name: {self.name})"
class Course:
    def __init__(self, course_code, course_name, teacher=None):
        self.course_code = course_code
        self.course_name = course_name
        self.teacher = teacher
        self.students = []
    def set_teacher(self, teacher):
        self.teacher = teacher
        teacher.assign_course(self)
    def add_student(self, student):
        self.students.append(student)
        student.enroll(self)
    def __str__(self):
        teacher_name = self.teacher.name if self.teacher else "Not Assigned"
        return f"{self.course_code} - {self.course_name} | Teacher: {teacher_name}"
if __name__ == "__main__":
    # Create teachers
    teacher1 = Teacher(101, "Mr. Smith")
    teacher2 = Teacher(102, "Ms. Johnson")
    # Create students
    student1 = Student(1, "Alice")
    student2 = Student(2, "Bob")
    student3 = Student(3, "Charlie")
    # Create courses
    math = Course("MATH101", "Mathematics")
    science = Course("SCI101", "Science")
    # Assign teachers to courses
    math.set_teacher(teacher1)
    science.set_teacher(teacher2)
    # Enroll students
    math.add_student(student1)
    math.add_student(student2)
    science.add_student(student2)
    science.add_student(student3)
    # Display course details
    print(math)
    print("Students enrolled:")
    for s in math.students:
        print("-", s.name)
    print("\n", science)
    print("Students enrolled:")
    for s in science.students:
        print("-", s.name)
