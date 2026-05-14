nums=[2,4,6,8]
result=list(map(lambda x: x**2, nums))
print(result)


nums = [1, 5, 8, 10, 3, 12]
result1=list(filter(lambda x:x%2==0,nums))
print(result1)



names = ["raj", "ram", "sita"]
result2=list(map(lambda x:x.upper(),names))
print(result2)


names = ["raj", "ram", "sita"]
result2=list(map(lambda x:x.lower(),names))
print(result2)

