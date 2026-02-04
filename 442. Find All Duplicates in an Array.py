# leetcode
# both of the solutions didn't beat 100% - there is something wrong
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # we should make sure the accessing element is minimized by 1 and abs() after modification
        result = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                result.append(abs(nums[i]))
            nums[abs(nums[i])-1] *= -1 

        return result

        # # using sliding window / 2-pointer
        # left = 0
        # right = 1
        # if len(nums) == 1:
        #     return []
        
        # nums.sort()
        
        # result = []
        # while right < len(nums):
        #     if nums[left] == nums[right]:
        #         result.append(nums[left])
        #     left += 1
        #     right += 1
        
        # return result
