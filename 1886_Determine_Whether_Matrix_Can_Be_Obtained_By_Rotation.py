# leetcode
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat != target:
                mat = [list(col) for col in zip(*mat[::-1])]
            else:
                return True
        return False