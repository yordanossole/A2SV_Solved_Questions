# leetcode
from collections import deque
class Solution:
    def flip(self, nums, start):
        for i in range(start, start+3):
            nums[i] = 1 - nums[i]
    
    def minOperations(self, nums: List[int]) -> int:
        counter = 0
        n = len(nums)

        for i in range(n-2):
            if nums[i] == 0:
                self.flip(nums, i)
                counter += 1

        return counter if all(n == 1 for n in nums) else -1