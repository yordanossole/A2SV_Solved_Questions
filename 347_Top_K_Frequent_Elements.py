# leetcode
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_counter = Counter(nums)
        result = []
        for num, f in n_counter.most_common(k):
            result.append(num)
        return result
        # # one linner
        # return [i[0] for i in Counter(nums).most_common(k)]