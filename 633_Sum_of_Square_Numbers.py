# leetcode
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left <= right:
            if c == left**2 + right**2:
                return True
            elif c < left**2 + right**2:
                right -= 1
            else:
                left += 1
        return False