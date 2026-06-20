n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter numbers: ").split()))

nums.sort()

print("Second Largest:", nums[-2])
