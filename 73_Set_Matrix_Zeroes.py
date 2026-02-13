# leetcode
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_row = set()
        zero_col = set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_row.add(row)
                    zero_col.add(col)

        for row in range(rows):
            for col in range(cols):
                if row in zero_row or col in zero_col:
                    matrix[row][col] = 0
        
        return matrix
