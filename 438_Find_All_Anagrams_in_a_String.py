# leetcode
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram = Counter(p)
        k = len(p)
        window = Counter(s[:k])
        left = 0
        result = []

        if anagram == window:
            result.append(left)

        for right in range(k, len(s)):
            window[s[right]] += 1
            window[s[left]] -= 1
            left += 1
            
            if window == anagram:
                result.append(left)

        return result