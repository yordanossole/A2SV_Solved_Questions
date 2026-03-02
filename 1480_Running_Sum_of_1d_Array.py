# leetcode
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        cur_sum = 0
        for num in nums:
            cur_sum += num
            prefix.append(cur_sum)
        return prefix