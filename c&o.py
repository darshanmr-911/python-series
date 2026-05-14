'''Create a class called Student with the following:
🔹 Requirements:
Create a constructor (__init__) that takes:
name
marks
Create a method called display() that prints:
Name: <name>
Marks: <marks>
Create an object:
s1 = Student("Rahul", 85)
Call the method to display output.
🧾 Expected Output:
Name: Rahul
Marks: 85'''
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Student",self.name)
        print("Marks",self.marks)
student1=student("darshan",100)
student1.display()