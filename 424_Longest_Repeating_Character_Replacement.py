# leetcode
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window = defaultdict(int)
        result = 0
        max_freq = 0
        
        for right in range(len(s)):
            window[s[right]] += 1
            max_freq = max(max_freq, window[s[right]])

            if (right - left + 1) - max_freq > k:
                window[s[left]] -= 1
                left += 1
            
            result = max(result, right-left+1)
        
        return result