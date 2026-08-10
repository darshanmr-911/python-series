'''Create a Class:

Write a class Mobile with attributes brand and price.
Create two objects of the class and display their attributes using a method.'''

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print(f"Brand = {self.brand}")
        print(f"Price = {self.price}")


m1 = Mobile("Samsung", 20000)
m2 = Mobile("iPhone", 50000)

m1.display()
m2.display()
    