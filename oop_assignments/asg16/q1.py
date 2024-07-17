class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter and Setter for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # Getter and Setter for age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__major = major

    # Getter and Setter for student_id
    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = student_id

    # Getter and Setter for major
    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, major):
        self.__major = major

class Professor(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__department = department

    # Getter and Setter for employee_id
    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter and Setter for department
    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, department):
        self.__department = department

class University:
    def __init__(self):
        self.students = []
        self.professors = []

    def add_student(self, student):
        self.students.append(student)

    def add_professor(self, professor):
        self.professors.append(professor)

    def display_all_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Student ID: {student.student_id}, Major: {student.major}")

    def display_all_professors(self):
        for professor in self.professors:
            print(f"Name: {professor.name}, Age: {professor.age}, Employee ID: {professor.employee_id}, Department: {professor.department}")

# Example usage
university = University()

# Adding students
student1 = Student("Alice", 20, "S1001", "Computer Science")
student2 = Student("Bob", 22, "S1002", "Mathematics")
university.add_student(student1)
university.add_student(student2)

# Adding professors
professor1 = Professor("Dr. Smith", 45, "P2001", "Physics")
professor2 = Professor("Dr. Johnson", 50, "P2002", "Chemistry")
university.add_professor(professor1)
university.add_professor(professor2)

# Display all students
print("Students:")
university.display_all_students()

# Display all professors
print("\nProfessors:")
university.display_all_professors()
