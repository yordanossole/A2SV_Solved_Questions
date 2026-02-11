# leetcode
from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        
        result = []
        count = Counter(changed)

        for num in sorted(changed):
            if count[num] == 0:
                continue

            if count[num*2] == 0:
                return []

            result.append(num)
            count[num] -= 1
            count[num*2] -= 1

        return result