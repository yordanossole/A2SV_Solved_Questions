# leetcode
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # better time complexity with 98.16 % beats
        return Counter(s) == Counter(t)

        # # short option
        # return sorted(s) == sorted(t)

        # if "".join(sorted(s)) == "".join(sorted(t)):
        #     return True
        # else:
        #     return False

        # # bruteforce
        # if len(s) != len(t):
        #     return False
        
        # counter = dict()

        # for char in s:
        #     counter[char] = counter.get(char, 0) + 1
        
        # for char in t:
        #     if char not in counter or counter[char] == 0:
        #         return False
        #     counter[char] -= 1
        
        # return True