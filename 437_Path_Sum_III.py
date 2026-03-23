# leetcode
# https://leetcode.com/problems/path-sum-iii/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = 0
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, targetSum):
            if not root:
                return
            
            check(root, targetSum)
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            
        def check(root, targetSum):
            if not root:
                return
            
            if root.val == targetSum:
                self.path += 1
            
            check(root.left, targetSum - root.val)
            check(root.right, targetSum - root.val)
        
        dfs(root, targetSum)
        return self.path
