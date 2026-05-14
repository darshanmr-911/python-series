try:
    numerator=float(input("Enter the numerator values:"))
    denominator=float(input("Enter the denominator values:"))
    quotient=numerator/denominator
    print(f"The quotient is:{quotient}")
except ValueError:
    print("Invalid input Please Enter the valid numbers")
except ZeroDivisionError:
    print("Invalid input please enter non zero denominator")



# Take two integers as input and print the result of division.
# 👉 If the second number is 0, handle the error and print:

try:
    x=int(input("Enter the number for x:"))
    y=int(input("Enter the number for y"))
    z=x/y
    print(f"The value of z is:{z}")
except ZeroDivisionError:
    print("Invalid input please enter the non zero numbers")

# Take an integer input from the user.
# 👉 If the user enters something that is not a number, print:

try:
    num=int(input("Entyer the number:"))
except ValueError:
    print("Invalid input")



l=[10,20,30,40,50]
try:
    index= int(input("Enter the index of the list:"))
    print(l[index])
except IndexError:
    print("Invalid index please enter the valid index")
except ValueError:
    print("Invalid input please enter the valid index")

