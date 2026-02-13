# leetcode
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        counter = 0

        for row in range(rows-1,-1,-1):
            for col in range(cols):
                if grid[row][col] < 0:
                    counter += cols - col
                    break

        return counter
