# leetcode
from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        temp = []
        for row in responses:
            temp.extend(set(row))
        
        count = Counter(temp)

        max_freq = max(count.values())
        max_freq_res = [response for response, freq in count.items() if freq == max_freq]

        return min(max_freq_res)       