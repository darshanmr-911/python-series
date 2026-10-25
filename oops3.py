# Method Definition:

# Define a class Student with attributes name and marks.
# Write a method display_info() that prints the student's name and marks.
# Create multiple objects of the Student class and call the method on each.


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Marks:{self.marks}")
        
s1 = Student("Darshan",90)
s2  = Student("Pooja",94)
s3 = Student("Hima",98)

s1.display_info()
s2.display_info()
s3.display_info()