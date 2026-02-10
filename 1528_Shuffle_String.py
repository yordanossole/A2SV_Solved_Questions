# leetcode
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [0] * len(s)
        for char, i in zip(s,indices):
            result[i] = char

        return "".join(result) 
     