'''Greet Function: Write a function greet() that takes no arguments and prints a greeting message.'''
def greet():
    print("Hello,World!")
greet()
print()

'''Parameterized Greet: Write a function greet_user() that takes a name as input and prints a custom greeting.'''
def greet_user(name):
    print(f"My name is {name}")
greet_user("Darshan")
print()

'''Sum Function: Write a function add_numbers(a, b) that returns the sum of two numbers. Call this function with different values.'''
def sum(a,b):
    return a+b
print(sum(4,5))

'''Even or Odd Function
Write a function check_even_odd(n) that prints whether a number is even or odd.'''
def even_num(n):
    if n%2==0:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")
even_num(2)
even_num(3)
print()

'''Maximum of Two Numbers
Write a function find_max(a, b) that returns the larger number.'''
def find_max(a,b):
    if a>b:
        return a
    else:
        return b
print(find_max(2,3))
print(find_max(50,20))
print()

'''Square Function
Write a function square(n) that returns the square of a number.'''
def square(n):
    return n*n
print("The square of the number is:",square(5))
print()

'''    Write a function simple_interest(p, r, t) that returns simple interest.
    Formula: SI = (p × r × t) / 100'''
def simple_intrest(p,q,r):
    return (p*q*r)/100
print(simple_intrest(1000,50,5))
print()

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print()
