# leetcode
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        result = []

        row, col = 0, 0
        
        for _ in range(rows*cols):
            result.append(mat[row][col])

            if (row + col) % 2:
                # if odd go downward
                if row == rows - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    col -= 1
                    row += 1
            else:
                # if even go upward
                if col == cols - 1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1

        return result
