# row=int(input("Enter the number of rows:"))
rows=5
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end="")
    print()

print()
rows=5
for i in range(rows+1):
    for j in range(i):
        print("*",end="")
    print()

print()
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()