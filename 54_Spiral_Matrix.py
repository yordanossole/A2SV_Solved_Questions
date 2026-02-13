# leetcode
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        # pointers
        top = 0
        left = 0
        bottom = rows-1
        right = cols-1

        result = []

        while left <= right and top <= bottom:
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1

            for j in range(top, bottom+1):
                result.append(matrix[j][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                for j in range(bottom, top-1, -1):
                    result.append(matrix[j][left])
                left += 1

        return result
