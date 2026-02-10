# leetcode
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:          
        hashmap = {}
        for num in nums:
            comp = target - num
            if comp in hashmap:
                return [i, hashmap[comp]]
            hashmap[num] = i
            i+=1

        # return []
        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i

        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap and hashmap[complement] != i:
        #         return [i, hashmap[complement]]

        # return []

# Bruteforce
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
