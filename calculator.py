num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print("Please select the operator '+'   '-'     '*'     '/'")
op=input("Enter the the operator:")
match op:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case  "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Invalid operator")