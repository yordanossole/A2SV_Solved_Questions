# leetcode
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        check = n//3
        n_counter = Counter(nums)
        result = []
        for num, f in n_counter.items():
            if f > check:
                result.append(num)
        return result