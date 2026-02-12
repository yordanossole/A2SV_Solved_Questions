# leetcode
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        return any(freq for freq in count.values() if freq > 1)
