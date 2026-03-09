# leetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # cur = node
        # while cur.next.next:
        #     nxt = cur.next
        #     cur.val = nxt.val
        #     cur = cur.next
        # nxt = cur.next
        # cur.val = nxt.val
        # cur.next = None

        # with out loop
        node.val = node.next.val
        node.next = node.next.next

        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """