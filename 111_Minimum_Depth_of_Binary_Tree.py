# leetcode
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: # incase the root node is null (empty tree)
            return 0
        if not root.left and not root.right:
            return 1
        
        l = float("inf")
        r = float("inf")

        if root.left:
            l = 1 + self.minDepth(root.left)
        if root.right:
            r = 1 + self.minDepth(root.right)
        return min(l, r)