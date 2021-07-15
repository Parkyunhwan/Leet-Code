# My Solution (재귀)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        def getDepth(node, depth, max_depth):
            if not node:
                max_depth = max(depth, max_depth)
                return max_depth
            max_depth = getDepth(node.left, depth + 1, max_depth)
            max_depth = getDepth(node.right, depth + 1, max_depth)
            return max_depth
        return getDepth(root, 0, max_depth)

# Best 재귀 솔루션
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# My Solution (BFS 반복 구조)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)): # 현재 레벨에서 모든 노드 만큼 반복
                cur_node = queue.popleft()
                if cur_node.left:
                    queue.append(cur_node)
                if cur_node.right:
                    queue.append(cur_node)
        return depth



