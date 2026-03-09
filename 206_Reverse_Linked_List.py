# leetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_nxt_node = None

        while head:
            tmp_head = head.next
            head.next = new_nxt_node
            new_nxt_node = head
            head = tmp_head
        
        return new_nxt_node