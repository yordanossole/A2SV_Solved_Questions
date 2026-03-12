# leetcode
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # mono increasing
        for num in nums:
            if stack and stack[-1] > num:
                return True
            stack.append(num)
        return False