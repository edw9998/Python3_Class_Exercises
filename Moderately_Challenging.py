class Person:
    # Parent Class Attributes May Not Be Set To Private
    def __init__(self, name = "Lily", address = "King Alexander St."):
        self.name = name
        self.address = address

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_address(self, new_address):
        self.address = new_address

    def get_address(self):
        return self.address

    def __str__(self):
        return f"Person Information:\nName = {self.name}\nAddress = {self.address}"

class Teacher(Person):
    def __init__(self, name = "Ms. Anderson", address = "241 Ashford St."):
        super().__init__(name, address)
        self.__numcourses = 0
        self.__courses = []

    def to_course_details_str(self):
        # Return Available Courses Here.
        print(f"Available Courses = {self.__courses}")
        return f"Teacher Information:\nTeacher Name = {self.name}\nTeacher Address = {self.address}"

    def add_course(self):
        course = str(input("Add This Course = "))
        for lesson in self.__courses:
            if lesson == course:
                raise Exception("This Course Has Been Added Previously.")
            else:
                self.__courses.append(course)

    def remove_course(self):
        insert_course = str(input("Remove This Course = "))
        for lesson in self.__courses:
            if lesson == insert_course:
                self.__courses.remove(lesson)
                print(f"{insert_course} Successfully Removed.")
            elif insert_course not in self.__courses:
                return False

class Student(Person):
    def __init__(self, name = "Lily", address = "King Alexander St."):
        super().__init__(name, address)
        self.__numcourses = 0
        self.courses = [] #str()
        self.grades = []  #int()

    def add_course_grade(self):
        course = input("Which Course ? ->")
        grade = eval(input("Enter Scoring Result = "))
        self.courses.append([course])
        self.grades.append([course, grade])

    def print_grades(self):
        return self.grades

    def get_average_grade(self):
        import statistics as st
        temp = []
        for el in self.grades:
            for pair in el:
                if type(pair) is int or type(pair) is float:
                    temp.append(pair)
        mean_res = st.mean(temp)
        return f"Your Average Grade Is : {mean_res}"

    def to_str(self):
        return f"Person Information:\nName = {self.name}\nAddress = {self.address}\nCourses = {self.courses}\nGrades = {self.grades}\nAverage_Grade = {self.get_average_grade()}"


        
                    
                    
        





            





