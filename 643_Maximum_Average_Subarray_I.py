# leetcode
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = cur_sum = sum(nums[:k])
        left = 0

        for right in range(k, len(nums)):
            cur_sum -= nums[left]
            cur_sum += nums[right]
            left += 1
            max_sum = max(max_sum, cur_sum)
        return max_sum / k