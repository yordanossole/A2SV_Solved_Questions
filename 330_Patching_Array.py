# leetcode
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        need, i, counter = 0, 0, 0

        while need < n:
            if i < len(nums) and nums[i] <= (need + 1):
                need += nums[i]
                i += 1
            else:
                need += (need + 1)
                counter += 1
            
        return counter