# leetcode
class Solution:
    def helper(self, nums, turn):
        l = len(nums)
        if l == 0:
            return False
        if l == 1:
            return nums[0]
        
        if l % 2:
            return self.helper(nums[1::2], abs(turn - 1))
        else:
            return self.helper(nums[turn::2], abs(turn - 1))

    def lastRemaining(self, n: int) -> int:
        # nums = [n for n in range(1, n+1)]
        nums = range(1, n+1)
        return self.helper(nums, 1)