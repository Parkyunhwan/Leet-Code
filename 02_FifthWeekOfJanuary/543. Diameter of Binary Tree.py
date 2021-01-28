class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def depth(p):
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.ans

class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.longest



