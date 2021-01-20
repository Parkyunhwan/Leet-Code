# 재귀 방법

# 노드를 교환하는 방법
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next
        return root.next

# 값만 교환하는 방법
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head