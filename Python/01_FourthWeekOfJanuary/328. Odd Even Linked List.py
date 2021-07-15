# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head:
            return head
        odd = head
        even = even_head = head.next

        while even and even.next:
            even.next, odd.next = even.next.next, odd.next.next
            even, odd = even.next, odd.next

        odd.next = even_head
        return head