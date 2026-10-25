s={10,20,30}
print(list(s))
print()

a={"a","b","c","d"}
print(len(list(a)))
print()

s={5,1,9,3}
print(sorted(list(s)))
print()


s={1,2,3,4,5,6,6}
l=list(s)
for i in l:
    i%2==0
    print(i,end=" ")
print()

s={2,3,4,7,8,9,10}
print([j for j in s if j%2==0])
print()

s={5,12,7,18,2,20}
print([i for i in s if i>=10])


s={10,40,30,20}
marks=sorted(list(s))
print("The Second Largest marks:",marks[-2])


from os import remove


s={2,8,1,6,3,9}
print([i for i in s if i<=5])
















