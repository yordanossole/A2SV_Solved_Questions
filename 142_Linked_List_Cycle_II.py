# leetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tor = head
        rab = head

        while rab and rab.next:
            tor = tor.next
            rab = rab.next.next
            if tor == rab:
                break
        else:
            return None
        
        tor = head
        
        while rab != tor:
            rab = rab.next
            tor = tor.next

        return rab