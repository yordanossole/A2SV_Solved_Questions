# leetcode
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_c = Counter(s)
        for char in s:
            if s_c[char] == 1:
                return s.index(char)
        return -1
        