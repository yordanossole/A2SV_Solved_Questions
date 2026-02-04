# leetcode
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums) + 1
        # for i in range(n):
        #     if not i in nums:
        #         return i
        # x = set(nums)
        # y = set(range(n))
        # return y.difference(x).pop()
        n = len(nums)
        expectedSum = n * (n+1) // 2
        actualSum = sum(nums)
        return expectedSum - actualSum
