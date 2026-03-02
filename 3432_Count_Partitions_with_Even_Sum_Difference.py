# leetcode
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # running sum
        counter = 0
        total = sum(nums)
        n = len(nums)
        l = 0
        for i in range(n-1):
            l += nums[i]
            r = total - l
            if (l + r) % 2 == 0:
                counter += 1

        return counter

        # # prefix sum
        # prefix = []
        # cur_sum = 0
        # for num in nums:
        #     cur_sum += num
        #     prefix.append(cur_sum)
        
        # counter = 0
        # n = len(prefix)
        # for i in range(n-1):
        #     l = prefix[i]
        #     r = prefix[n-1] - l
        #     if (l + r) % 2 == 0:
        #         counter += 1

        # return counter