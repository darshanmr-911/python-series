x = int(input())
z = 0

while x > 0:
    i = x % 10

    # add i to z here
    z = z + i
    # remove the last digit from x here
    x = x // 10
print(f"Sum : {z}")