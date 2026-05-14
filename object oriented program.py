class car:
    def __init__(self,name,id,price,rented_days,price_per_day,status="available"):
        self.name=name
        self.id=id
        self.price=price
        self.rented_days=rented_days
        self.price_per_day=price_per_day
        self.status=status
    def display_details(self):
        print(f"Name:{self.name},Car id:{self.id},self.status:{self.status},Status:{self.status}")
    def updated_status(self,new_status):
        self.status=new_status
        print(f"{self.id} is updated {self.status}")
    def calculate_rent(self):
        total_price=self.rented_days*self.price_per_day

car1=car("BMW","M4",450000,3,1500,"avilable")

car1.updated_status("rented")
car1.calculate_rent()
car1.display_details()





class Student:
    def __init__(self, marks, name, age, gender, sem, usn):
        self.name = name
        self.age = age
        self.gender = gender
        self.usn = usn
        self.marks = marks
        self.sem = sem

    def display(self):
        print(f"The Name of the student is {self.name},he has {self.age} old and and he has{self.gender} gendere .The USN of the stident is {self.usn} ans SEM is {self.sem} .the marks of the student is {self.marks}")

student1 = Student(90, "Darshan", 20, "Male", 4, "1AR24AI011")
student1.display()