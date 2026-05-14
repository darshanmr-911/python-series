
#Logical Operator Practice: Write a Python program that takes two numbers as input from the user and checks if:
#1.Both numbers are greater than 10 (using and).
#2.At least one of the numbers is less than 5 (using or).
#3.The first number is not greater than the second (using not).


a=int(input("Enter the number for a:\n"))
b=int(input("Enter the number for b:\n"))
print(a>10 and b>10)
print(a<5 or b>10)
print(not(a>b))



#2.Comparison Operator Challenge: Create a Python program that asks the user for their age and prints:
#"You are an adult" if the age is greater than or equal to 18.
#"You are a minor" if the age is less than 18.
#Use >= and < comparison operators.


age=int(input("Enter your age:\n"))
if age>=18:
    print("Your are adult")
elif age<18:
    print("your minor")




#Membership Operator Exercise: Write a Python program that:
#Takes a string as input from the user.
#Checks if the letter 'a' is in the string (using in).
#Checks if the string doesn't contain the word "Python" (using not in).


text = input("Enter a string: ")
if 'a' in text:
    print("The letter 'a' is present in the string.")
else:
    print("The letter 'a' is NOT present in the string.")
if "Python" not in text:
    print("The word 'Python' is NOT in the string.")
else:
    print("The word 'Python' IS present in the string.")


