# leetcode
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        n = len(needle)
        h = len(haystack)
        for i in range(h - n + 1):
            if needle == haystack[i:i+n]:
                return i
            i += 1
        return -1