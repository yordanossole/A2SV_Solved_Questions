# leetcode
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0
        def check(root, level):
            nonlocal res
            if not root:
                return
            if level == 3:
                res += root.val
                return
            check(root.left, level + 1)
            check(root.right, level + 1)
        
        def find(root):
            if not root:
                return
            
            if root.val % 2 == 0:
                check(root, 1)
            find(root.left)
            find(root.right)
        
        find(root)
        return res