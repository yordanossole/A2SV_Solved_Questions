# leetcode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # with out dummy head
        if not head:
            return head
        cur_node = head
        prev_node = None

        while cur_node:
            if cur_node.val == val:
                if not prev_node:
                    head = cur_node.next
                else:
                    prev_node.next = cur_node.next 
            else:
                prev_node = cur_node
            cur_node = cur_node.next

        return head

    def removeElementsWithDummyHead(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode("dummy")
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next

        # with out prev
        # cur = dummy

        # while cur.next:
        #     if cur.next.val  == val:
        #         cur.next = cur.next.next
        #     else:
        #         cur = cur.next
        # return dummy.next