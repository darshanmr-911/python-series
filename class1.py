class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        print("Name of the student:",self.name)
        print("Marks of the student:",self.marks)
r1=student("Darshan",90)
r1.result()