# 전위노드와 중위노드의 순서가 있으면 트리의 구조를 복원할 수 있다.
# 전위노드는 항상 중위노드의 분할 지점이 된다.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node