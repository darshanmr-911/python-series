def greet():
    print("Hello, world:")
greet()
print()

def marriage(boy,girl):
    print(f"{boy} marriage {girl}")
marriage("X","Y") #positional argument is used to pass the arguments to the function in the order of the parameters
marriage(boy="X",girl="Y") #keyword argument is used to pass the arguments to the function by the name of the parameter

def tables(numbers):
    for i in range(1,11):
        print(f"{numbers}X{i}={numbers*i}")
tables(1)
print()

def marriage(boy,girl="girl"): #default argument is used to pass the arguments to the function by the name of the parameter
    print(f"{boy} marriage {girl}")
marriage(boy="X")
print()

def fun(num):
    print(str(num)*num)
    print(str(num)*3)
fun(5)
print()

<<<<<<< HEAD
=======
def sum(a,b=0):
    return a+b
c=sum(3)
print(c)
print()


>>>>>>> master
#return type function
def fun(num):
    return int(str(num)*5)
a=fun(1)
b=100
print(a+b)
print()


def funn(num):
    return int(num*num)
a=funn(10)
b=10
print(a+b)

<<<<<<< HEAD

def name():
    x="Darshan" #local var
    print(y)

y="pavan"   #global variable
print(x)
print(y)
=======
name = "Global Name"
def greet():
    name = "Local Name"
    print(name)
greet()  # Prints local variable
print(name)  # Prints global variable
>>>>>>> master
