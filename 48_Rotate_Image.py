# leetcode
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        # transpose in place
        for row in range(rows):
            for col in range(row+1, cols): # starts after the main diagonal everytime
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        # reflect in place
        for row in range(rows):
            for col in range(cols//2): # iterate only to the half of cols
                matrix[row][col], matrix[row][cols-col-1] = matrix[row][cols-col-1], matrix[row][col]
        
        return matrix
