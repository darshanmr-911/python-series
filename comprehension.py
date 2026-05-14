l=(3,67,85,99)
count=0
for i in l:
    count=count+i
print(count)


d=(3,67,85,99)
dl=[]
for i in d:
    dl.append(i*2)
    print(dl)
print(dl)
print()

fruits=["apple","banana","grapes","orange"]
for i in fruits:
    print(i)
print()

students=[("Darshan",85),("Pavan",90),("Prathibha",95)]
for name, mark in students:
    print(f"{name}--->{mark}")
print()

std=["darshan","pavan","prathibha"]
marks=[85,90,95]
result={}
for index,name in enumerate(std):
    result[name]=marks[index]
print(result)
print()

students=["darshan","pavan","prathibha"]
marsks=[85,90,95]
std_marks={}
for i in range(1,len(students),2):
    std_marks[students[i]]=marks[i]
print(std_marks)
print()


car=["AUDI","BMW","MERCEDES","FERRARI","PORSCHE"]
model=["A4","X5","C-CLASS","488","911"]
car_model={}
for cars in range(len(car)):
    car_model[car[cars]]=model[cars]
print(car_model)
print()


fruits=["apple","banana","grapes","orange"]
l=[]
for fruit in fruits:
    l.append(fruit.upper())
print(l)
print()

#using list comprehension
fruits=["apple","banana","grapes","orange"]
dl=[fruit.upper() for fruit in fruits]
print(dl)
print()

number=[5,6,3,9,3,5]
nums=[num**2 for num in number]
print(nums)
print()

number=[5,6,3,9,8,5]
nums=[num for num in number if num%2==0]
print(nums)
print()

number=[num for num in range(1,11)]
nums=[num for num in number if num%2==0]
print(nums)
print()

name=["darshan","pavan","prathibha"]
names=[names[3] for names in name ]
print(names)
print()

#Dictionary Comprehension
names=["darshan","pavan","prathibha"]
names={name:len(names) for name in names}
print(names)
print()

marks={"darshan":85,"pavan":90,"prathibha":95}
final_result={name:mark for name,mark in marks.items() if mark>=90}
print(final_result)

#list input for user
#first we will take the input as string and then we will split the string to get the list of numbers
n=input("Enter the number: ")
x=n.split()
print(x)
print()


s=input("Enter the string:")
x=[int(n) for n in s.split()]
print(x)
print()

name=[names for names in input("Enter your names: ").split()] 
print(name)
