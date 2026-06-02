import random
guess=random.randint(1,100)
limit=5
for i in range(limit):
    number=int(input("Enter the number between 1 to 100:"))
    if number==guess:
        print("You guessed the correct number",guess)
        break
    elif number<guess:
        print("Too low")
    elif number>guess:
        print("Too high")
    else:
        print("Invalid number")




