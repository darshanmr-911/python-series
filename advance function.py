import re


def add(*a):
    print(type(a))
add(1,2,3,4,5)
print()

#Variable-Length Arguments
def add(*numbers):
    return sum(numbers)
print(add(1,2,3,4,5))
print()

#Keyword Arguments(variable lenth arugument)
def student_into(**info):
    print(info)
    for keys,values in info.items():
        print(f"{keys}:{values}")
student_into(Name="Darshan",age=20,sem=4)
print()

#Lambda Functions
add=lambda a,b: a+b
print(add(2,3))
print()

double=lambda x: 2*x
print(double(5))
print()

student=[
    {"name":"drashan","marks":50},
    {"name":"pavan","marks":90},
    {"name":"navya","marks":80}
]
student.sort(key=lambda x:x["marks"])
print(student)
print()

student=[
    {"name":"drashan","marks":50},
    {"name":"pavan","marks":90},
    {"name":"navya","marks":80}
]
student.sort(key=lambda x:x["marks"],reverse=True)
print(student)
print()


car=[
    {"name":"bmw","price":2000000},
    {"name":"audi","price":3000000},
    {"name":"mercedes","price":4000000} 
]
car.sort(key=lambda x:x["price"])
print(car)
print()

#recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
print()

#nested function
def calculate(a,b):
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    return add(a,b),sub(a,b),mul(a,b),div(a,b)
print(calculate(6,7))
print()

def outer_function(name):
    def inner_function():
        print(f"Hello, {name}!")
    inner_function()

outer_function("Darshan")