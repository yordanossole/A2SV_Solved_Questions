# leetcode
class NumArray:

    def __init__(self, nums: List[int]): 
        self.nums = nums
        self.prefix = []
        cur_sum = 0
        for num in self.nums:
            cur_sum += num
            self.prefix.append(cur_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - self.prefix[left] + self.nums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)