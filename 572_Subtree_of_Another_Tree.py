# leetcode
# https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return isSame(p.left, q.left) and isSame(p.right, q.right)

        def findRoot(root, sRoot):
            if not root:
                return
            
            if root.val == sRoot.val:
                if isSame(root, sRoot):
                    return True
            
            return findRoot(root.left, sRoot) or findRoot(root.right, sRoot)
            
        return True if findRoot(root, subRoot) else False