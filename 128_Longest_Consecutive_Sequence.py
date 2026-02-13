# leetcode
from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)

        for num in s:
            if num - 1 not in s:
                cur = num
                length = 1
                while cur+1 in s:
                    length += 1
                    cur += 1

                longest = max(longest, length)
                
        return longest