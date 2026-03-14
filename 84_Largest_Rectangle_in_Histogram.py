# leetcode
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            cur = i
            while stack and heights[i] < stack[-1][1]:
                ind, h = stack.pop()
                w = i - ind
                cur = ind
                max_area = max(max_area, w*h)
            stack.append((cur, heights[i]))
            
        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)
        
        return max_area