from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)
        return [num for num, freq in count.items() if freq > n//3]