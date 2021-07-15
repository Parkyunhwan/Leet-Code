'''
중위 순회 & 재귀 & 클래스 변수
'''
class Solution:
    value = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.value += root.val
            root.val = self.value
            self.bstToGst(root.left)
        return root