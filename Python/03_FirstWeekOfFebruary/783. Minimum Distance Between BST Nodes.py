# 중위 순회 문제
# 재귀 풀이 - 재귀의 흐름대로 진행했을 때 현재 노드와 이전 노드의 차이를 구하는 것이 BST에서는 노드간 최소 거리를 구하는 방법이다.
class Solution:
    min_value = sys.maxsize
    prev = -sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(root):
            if root.left:
                dfs(root.left)

            self.min_value = min(self.min_value, abs(root.val - self.prev))
            self.prev = root.val

            if root.right:
                dfs(root.right)

        dfs(root)
        return self.min_value


# 반복 구조 코드
# 흐름을 따라가다 보면 중위 순회에 대해 직관적으로 느낄 수 있다.
class Solution:

    def minDiffInBST(self, root: TreeNode) -> int:
        prev = -sys.maxsize
        min_value = sys.maxsize

        stack = []
        node = root

        while stack or node:
            while node:  # 현재 노드의 모든 왼쪽 노드를 먼저 스택에 추가함
                stack.append(node)
                node = node.left

            node = stack.pop()  # 추가된 왼쪽 리프 노드 부터 꺼냄

            result = min(min_value, node.val - prev)  # 현재노드에서 이전 노드(현재 노드 보다 작은 노드)와 비교 하게 됨
            prev = node.val

            node = node.right  # 현재노드의 오른쪽 노드 추가
        return result