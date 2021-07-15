# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        root = start = ListNode(None)
        root.next = head
        for _ in range(m - 1):
            start = start.next
        end = start.next

        for _ in range(n - m):
            tmp = start.next  # 범위 내 가장 앞에 있던 원소 (start.next)
            start.next = end.next  # 가장 뒤에 있던 원소 (end.next)
            end.next = end.next.next  # 가장 뒤에 있던 원소와 연결 대신 그 뒤와 연결
            start.next.next = tmp  # 가장 뒤에 잇던 원소의 다음에 가장 앞에 있던 원소를 연결

        return root.next