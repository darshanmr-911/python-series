my_list=[5,3,1,2,4]
my_list.append(6)
my_list.remove(3)
my_list.sort()
my_list.reverse()
my_list[4]=7
print(my_list)

list=[2,4,6,8]
total=0
for i in list:
    total+=i         #return the sum of all the numbers in the list
print(total)

list1=[5,2,9,1,7]
large=list1[0]       #initialize the variable to the first element of the list 
for i in list1:
    if i>large:
        large=i
print(large)


list2=[1,2,3,4,5,6]
my_list2=0
for i in list2:
    if i%2==0:
        my_list2+=1       #return the count of even numbers in the list
print(my_list2)



