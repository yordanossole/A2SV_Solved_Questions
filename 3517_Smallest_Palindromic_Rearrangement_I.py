# leetcode
from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        count = dict(sorted(count.items()))
        left = []
        right = []
        middle = ""
        for char in count:
            freq = count[char]
            if (freq % 2):
                middle = char
                left.append(char*(freq//2))
                right.append(char*(freq//2))
            else:
                left.append(char*(freq//2))
                right.append(char*(freq//2))

        if middle:
            left.append(middle)
        
        return "".join(left) + "".join(right[::-1])