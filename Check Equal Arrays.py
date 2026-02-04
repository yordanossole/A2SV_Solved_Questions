# gfg
class Solution:
    def checkEqual(self, a, b) -> bool:
        return True if a.sort() == b.sort() else False
        