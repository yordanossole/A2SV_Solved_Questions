# leetcode
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        counter = 0
        while target > 0:
            if maxDoubles == 0:
                break
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            counter += 1
        
        return counter + target - 1