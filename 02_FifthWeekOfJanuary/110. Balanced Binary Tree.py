# 기존 뎁스를 구하던 식에서 좀 더 변형한 코드..
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getDepth(node):
            if not node:
                return 0
            left = getDepth(node.left)
            right = getDepth(node.right)

            # 핵심 조건문 이미 리프노드쪽에서 조건이 맞지 않으면 계속 -1을 반환
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            # 평범한 경우엔 이전까지 뎁스에 현재 노드를 더해 + 1을 해줌.
            return max(left, right) + 1

        return getDepth(root) != -1