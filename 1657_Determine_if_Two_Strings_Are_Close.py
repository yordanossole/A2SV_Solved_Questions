# leetcode
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        word1_count = Counter(word1)
        word2_count = Counter(word2)
        return sorted(word1_count.keys()) == sorted(word2_count.keys()) and sorted(word1_count.values()) == sorted(word2_count.values())
