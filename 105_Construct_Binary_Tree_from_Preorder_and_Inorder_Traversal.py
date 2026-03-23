# leetcode
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        index_map = {v:i for i, v in enumerate(inorder)}

        def spliter(start, end):
            if start > end:
                return
            
            val = preorder[self.i]
            self.i += 1
            root = TreeNode(val)

            mid = index_map[val]
            root.left = spliter(start, mid-1)
            root.right = spliter(mid+1, end)
            return root
        
        return spliter(0, len(inorder)-1)