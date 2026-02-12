# leetcode
from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        left = 0
        right = 1

        count = Counter(s)
        
        while left<len(s) and right<len(s):
            if int(s[left]) == count[s[left]] and int(s[right]) == count[s[right]] and s[left] != s[right]:
                return s[left:right+1]
            left += 1
            right += 1
        return ""
