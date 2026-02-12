# leetcode
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)

        result = []
        for char, freq in char_count.most_common():
            result.append(char*freq)
            
        return "".join(result)
        
