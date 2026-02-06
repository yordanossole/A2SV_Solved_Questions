# leetcode
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # this one is more optimized by C based loop not python loop 
        # but the O() is the same
        for i in range(left, right+1):
            if not any(l <= i <= r for l, r in ranges):
                return False
        return True

        # # python based implementation
        # for i in range(left, right + 1):
        #     for l, r in ranges:
        #         if l <= i <= r:
        #             break
        #     else:
        #         return False
        # return True