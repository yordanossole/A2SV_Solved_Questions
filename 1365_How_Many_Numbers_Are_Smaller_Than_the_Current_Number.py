# leetcode
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # result = []

        # for i in range(len(nums)):
        #     counter = 0
        #     for j in range(len(nums)):
        #         if nums[j] < nums[i]:
        #             counter += 1
        #     result.append(counter)
        # return result

        # Optimized
        result = []
        s_nums = sorted(nums)

        for i in nums:
            result.append(s_nums.index(i))
        return result