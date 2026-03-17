# leetcode
class Solution:            
    def predictTheWinner(self, nums: List[int]) -> bool:
        def choose(l, r):
            if l == r:
                return nums[l]
            return max(nums[l] - choose(l+1, r), nums[r] - choose(l, r-1))
        return choose(0, len(nums)-1) >= 0