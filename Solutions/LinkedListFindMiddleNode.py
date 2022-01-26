Solution 1: using 2 pointers 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer_1 = pointer_2 = head
        while pointer_2.next:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next.next if pointer_2.next.next else pointer_2.next
        return pointer_1

Solution 2: Using 1 pointer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        start_count = 0
        len_of_linked_list = 0
        while head.next:
            head = head.next
            len_of_linked_list += 1
        if len_of_linked_list % 2 == 0:
            desired_mid = len_of_linked_list // 2
        else:
            desired_mid = (len_of_linked_list // 2) + 1

        while start_count < desired_mid:
            start = start.next
            start_count += 1
        return start
