arr=[1,2,3,4,5]
sum=[]
total=0
for i in arr:
    total+=i
    sum.append(total)
print(sum)
print()

arr=[1,2,3,4,5]
arr1=[6,7,8,9,10]
sum=[]
total=0
for i in arr:
    for j in arr1:
        total+=i
        total+=j
        sum.append(total)
print(sum)
print()

count=0
sum1=[]
for i in arr:
    count+=i
print(count)
print()

count=0
sum1=[]
for i in arr:
    count+=i
    print(count,end=" ")