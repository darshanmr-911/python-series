# x="100"
# y=int(x)
# z=float(x)
# a=str(x)
# print(y,z,a)


#lists

# l=[]
# for i in range(1,10):
#     l.append(i)
# print(l)


'''List Manipulation Exercise:

Create a list of 5 items (strings or numbers).
Add a new item to the end of the list and another at the second position.
Remove the third item from the list.
Print the list after each operation.'''

item=['apple','banana','cherry','grapes','orange']
item.insert(5,'mango')
item.remove('cherry')
print(item)

num=[1,2,3,4,5]
num.sort(reverse=True)
print(num)

print(item[0])
print(item[1])
item[2]='pineapple'
print(item)



karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa",
    "ramanagara": "ragi mudde",
    "mandya":"girmit"
}
n={"xyz":"zxu"}
karnataka_food.update(n)
karnataka_food["Bengaluru"]="ragi"
karnataka_food.pop("mandya")
print(karnataka_food.keys())
print(karnataka_food.values())
print(karnataka_food)


l=[1,2,3,4,5]
dl=[]
for i in l:
    dl.append(i*2)
print(dl)

items = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa",
    "ramanagara": "ragi mudde",
    "mandya":"girmit"
}
dl1=[]
for i in items.items():
    dl1.append(i)
print(dl1)


student=["darshan","deepak","ravi","kumar"]

marks=[80,90,70,60]

student_marks={}
for index,students in enumerate(student):
    student_marks[students]=marks[index]
print(student_marks)

for i in range(len(student)):
    student_marks[student[i]]=marks[i]
print(student_marks)

for i in range(1,len(student),2):
    student_marks[student[i]]=marks[i]
print(student_marks)


print()
l=[x for x in range(1,11)]

y=[x**2 for x in l if x % 2==0]

print(y)


# [exp for item in collection if condition]


