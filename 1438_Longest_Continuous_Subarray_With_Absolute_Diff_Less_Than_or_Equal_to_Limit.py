# leetcode
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc_q = deque()
        dec_q = deque()
        l = 0
        result = 0

        for r in range(len(nums)):
            while dec_q and dec_q[-1] < nums[r]:
                dec_q.pop()
            
            while inc_q and inc_q[-1] > nums[r]:
                inc_q.pop()
            
            dec_q.append(nums[r])
            inc_q.append(nums[r])

            while dec_q and inc_q and dec_q[0] - inc_q[0] > limit:
                if dec_q[0] == nums[l]:
                    dec_q.popleft()
                if inc_q[0] == nums[l]:
                    inc_q.popleft()
                l += 1
            
            result = max(result, r-l+1)

        return result            