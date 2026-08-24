class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # x = 0
        # for i in range(len(nums)):
        x = sum(nums)
        y = x % k
        return y
        