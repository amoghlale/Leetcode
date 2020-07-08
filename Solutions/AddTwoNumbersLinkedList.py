# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carrier=0) -> ListNode:
        val = l1.val + l2.val + carrier
        carrier = val // 10
        result = ListNode(val % 10)
        while l1.next is not None or l2.next is not None or carrier != 0:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            result.next = self.addTwoNumbers(l1.next, l2.next, carrier)
            return result
        return result
