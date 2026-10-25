def add(a = 0,b = 0):
    return a+b
print(add(2,3))

def sums(*nums):
    result = 0
    for num in nums:
        result += num
    return result
print(sums(1,2,3,4))