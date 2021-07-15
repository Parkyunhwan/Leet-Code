# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 리스트를 뒤집는 함수
    def reversedList(self, node: ListNode) -> ListNode:
        prev = None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 리스트로 변환하는 함수
    def convertToList(self, node: ListNode) -> list:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬의 리스트를 역연결리스트로 반환하는 함수
    def toReversedLinkedList(self, ret: str) -> ListNode:
        prev = None
        for r in ret:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.convertToList(self.reversedList(l1))
        b = self.convertToList(self.reversedList(l2))
        a = int(''.join(map(str, a)))
        b = int(''.join(map(str, b)))
        sm = a + b
        return self.toReversedLinkedList(str(sm))