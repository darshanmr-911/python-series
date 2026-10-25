#learning debugger 
i=0
while i<=10:
    print(i,end=" " )
    i+=2

for i in range(1,11):
    for j in range(1,2):
        print(f"{i}*{j}={i*j}")
print()


a,b=3,4
c=a
a=b
b=c
print(a,b)