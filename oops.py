class car:
    #Attribute
    def __init__(self,name,model,km):
        self.name=name
        self.model=model #Instance variable
        self.km=km
    def display(self):
        print(f"Car Brand:{self.name},Car Model:{self.model},Total KM:{self.km}")

#createing an object of the class
car1=car('BMW','M4',2025)
car1.display()
car2=car("Porshe",911,2026)
car2.display()
