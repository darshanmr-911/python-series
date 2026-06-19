num=int(input("Enter the number:"))

for i in range(2,num):
    if num%i==2:
        print("Not Prime")
        break
else:
    print("Prime")
