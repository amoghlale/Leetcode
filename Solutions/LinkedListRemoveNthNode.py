# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(-1)
        temp.next = head
        fast_pointer = slow_pointer = temp 
        i = 1
        while i <= n:
            fast_pointer = fast_pointer.next
            i += 1
        while fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        slow_pointer.next = slow_pointer.next.next
        return temp.next
