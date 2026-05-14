class emp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def increase(self):
        return self.salary+(self.salary*0.1)
    def details(self):
        print("Name of the employee:",self.name)
        print("Salary of the employee:",self.salary)
data=emp("Darshan",10000)
data.details()
print("New salary of the employee:",data.increase())
