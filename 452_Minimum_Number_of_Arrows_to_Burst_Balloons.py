# leetcode
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        arrow = 1
        end = points[0][1]
        for s, f in points:
            if s > end:
                arrow += 1
                end = f
        return arrow