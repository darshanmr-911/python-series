# Write your first Python program to print your name.
import re


print("Darshan")


# Arithmetic Practice: Write a Python program that performs basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers. Define the two numbers as variables within the code and print the results for each operation.
a=5
b=8
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#Swap Two Variables: Write a Python program that swaps the values of two variables with and without using a third variable.
a=5
b=9
print(f"a:{b},b:{a}")
a,b=b,a 

#Simple Greeting Program: Write a Python program that asks the user for their name and age, then prints a personalized greeting message. Use both the + operator and f-strings for output.
name=(input("Enter your name:"))
age=(int(input("Enter your age:")))
print(f"Hello,{name}! you are {age} years old.")

#String Manipulation Exercise: Write a Python program that:
# Takes a sentence as input from the user.
# Prints the sentence in all uppercase and lowercase.
# Replaces all spaces with underscores.
# Removes leading and trailing whitespace.
s=input("")
print(s.upper())
print(s.lower())
print(s.replace(" ","_"))
print(s.strip())

# Character Counter: Write a Python program that:
# Asks the user for a string.
# Prints how many characters are in the string, excluding spaces.
c=input("")
print(len(c.replace(" ","")))


# Escape Sequence Practice: Write a Python program that uses escape sequences to print the following output:
print("Hello\n\tWorld\nThis is blacklash:\\")

#  Write a Python program that takes two numbers as input from the user and checks if:
# Both numbers are greater than 10 (using and).
# At least one of the numbers is less than 5 (using or).
# The first number is not greater than the second (using not).
a=int(input())
b=int(input())
print(a>10 and b>10)
print(a<5 or b<5)
print(not a>b)

# Comparison Operator Challenge: Create a Python program that asks the user for their age and prints:

# "You are an adult" if the age is greater than or equal to 18.
# "You are a minor" if the age is less than 18.
# Use >= and < comparison operators.
age=int(input("Enter your age:"))
if age>=18:
    print("you are adult")
else:
    print("you are minor")


# Membership Operator Exercise: Write a Python program that:

# Takes a string as input from the user.
# Checks if the letter 'a' is in the string (using in).
# Checks if the string doesn't contain the word "Python" (using not in).
i=input("")
print("a" in i)
print("a" not in i)


# Bitwise Operator Task: Given two integers, write a Python program that:

# Prints the result of a & b, a | b, and a ^ b.
# Shifts the bits of a two positions to the left (a << 2).
# Shifts the bits of b one position to the right (b >> 1).

a,b=5,6
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b>>1)


l=[2,3,4,5,6]
l.append(7)
l.insert(2,"python")
l.remove(5)
print(l)

l1=[4,6,7,34,78,90]
l1.sort()
print(l1)
l1.reverse()
print(l1)





