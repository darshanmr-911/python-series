# nums = [3,9,7]
# k = 5
# x = 0
# for i in range(len(nums)):
     
#     x = x + nums[i]

# if x % k == 0:
#     print(x)


# print(nums[i] - 1)

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # x = 0
        # for i in range(len(nums)):
        x = sum(nums)
        y = x % k
        return y
        


