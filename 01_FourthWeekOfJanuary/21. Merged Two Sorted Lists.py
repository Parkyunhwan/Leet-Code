# Definition for singly-linked list.
# 기본적인 리스트 형태의 풀이
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = newNode = ListNode()
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    val = l1.val
                    l1 = l1.next
                else:
                    val = l2.val
                    l2 = l2.next
            elif l1:
                val = l1.val
                l1 = l1.next
            elif l2:
                val = l2.val
                l2 = l2.next
            newNode.next = ListNode(val)
            newNode = newNode.next
        return root.next