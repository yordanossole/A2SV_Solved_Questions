# leetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointer
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        # bruteforce
        # cur = head
        # leng = 0
        # while cur:
        #     cur = cur.next
        #     leng += 1
        
        # half = (leng//2) +1

        # cur = head
        # res = []
        # i = 1
        # while cur:
        #     if i == half:
        #         return cur
        #     i += 1
        #     cur = cur.next