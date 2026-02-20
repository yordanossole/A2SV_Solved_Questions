# leetcode
from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)
        ans = []

        for char in order:
            if s_count[char] != 0:
                ans.append(char*s_count[char])
                s_count[char] = 0
        
        for char in s_count.keys():
            if s_count[char] != 0:
                ans.append(char*s_count[char])
        
        return "".join(ans)