# Parent Class
class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_role(self):
        print("I am a User")


# Child Class - Student
class Student(User):

    def show_role(self):
        print("I am a Student")

    def study(self):
        print(self.name, "is studying")


# Child Class - Mentor
class Mentor(User):

    def show_role(self):
        print("I am a Mentor")

    def teach(self):
        print(self.name, "is teaching")


# Child Class - Admin
class Admin(User):

    def show_role(self):
        print("I am an Admin")

    def manage_platform(self):
        print(self.name, "is managing the platform")


# Create objects
student = Student("Arif", "arif@gmail.com")
mentor = Mentor("Rahul", "rahul@gmail.com")
admin = Admin("Amit", "amit@gmail.com")


# Display information
student.show_role()
student.study()

mentor.show_role()
mentor.teach()

admin.show_role()
admin.manage_platform()