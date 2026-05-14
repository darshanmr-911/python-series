#1st question
'''🟢 Question 1 (Easy)
Given:
arr1 = [1, 2]
arr2 = [3, 4]
👉 Task:
Combine both lists using itertools.chain()
Use accumulate() (default addition)
👉 Expected type of output:
Combined list
Running sum list'''

import itertools
import operator
arr1=[1,2]
arr2=[3,4]
x=list(itertools.chain(arr1,arr2))
print(x)
print(list(itertools.accumulate(x)))



#2nd question
'''Question 2 (Medium)
Given:
arr = [2, 3, 5, 2]
👉 Task:
Use accumulate() with multiplication
Print the result as a list
👉 Hint:
Use operator.mul'''

import itertools
import operator
arr = [2, 3, 5, 2]
print(list(itertools.accumulate(arr,operator.mul)))



#3rd Question
'''🔴 Question 3 (VTU Exam Level)
Given:
arr1 = [1, 3, 5]
arr2 = [2, 4]
arr3 = [6, 7]
👉 Task:
Combine all lists into one using chain()
Create 2 copies of the combined iterator using tee()
On first copy → apply accumulate() (addition)
On second copy → apply accumulate() (multiplication)
Print both results'''
import itertools
import operator
arr1 = [1, 3, 5]
arr2 = [2, 4]
arr3 = [6, 7]
combine=list(itertools.chain(arr1,arr2,arr3))
print(combine)      #Combine all lists into one using chain()
it1,it2=itertools.tee(combine,2)

print(list(itertools.accumulate(it1)))   #On first copy → apply accumulate() (addition)
print(list(itertools.accumulate(it2,operator.mul)))    #On second copy → apply accumulate() (multiplication)


'''⭐ Bonus (if you want challenge)
👉 Without using itertools, try to do Question 1 manually.'''
arr1=[1,2]
arr2=[3,4]
x=arr1+arr2
print(x)
result=[]
total=0
for i in x:
    total=total+i
    result.append(total)
print(result)

'''🟢 Practice Question (Manual – No itertools)
Given:
arr1 = [2, 3]
arr2 = [4, 1]
👉 Task:
Combine both lists manually (no itertools)
Find running sum manually using loop (like Step 2)'''
arr1=[2,3]
arr2=[4,1]
combine=arr1+arr2
print(combine)

result=[]
total=0
for num in combine:
    total+=num
    result.append(total)
print(result)

