# leetcode
# 10
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        result = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                i = 0
                total = 0

                for r in range(max(0, row-1), min(rows, row+2)):
                    for c in range(max(0, col-1), min(cols, col+2)):
                        i += 1
                        total += img[r][c]
                
                result[row][col] = total // i
        return result
       