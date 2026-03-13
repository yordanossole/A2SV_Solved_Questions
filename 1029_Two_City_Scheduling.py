# leetcode
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        map_ = []
        for a, b in costs:
            map_.append([b - a, a, b])

        map_.sort()
        ans = 0
        for i in range(n):
            if i < n // 2:
                ans += map_[i][2]
            else:
                ans += map_[i][1]
                
        return ans