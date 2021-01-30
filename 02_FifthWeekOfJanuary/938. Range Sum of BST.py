# MySoultion 재귀
class Solution:
    value = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root:
            if root.val > low:
                self.rangeSumBST(root.left, low, high)
            if root.val < high:
                self.rangeSumBST(root.right, low, high)
            if root.val >= low and root.val <= high:
                self.value += root.val
            return self.value

'''
좀 더 직관적인 반복구조! (stack 이용)
'''
class Solution:
    value = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack, sum = [root], 0

        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum

'''
stack만 큐 형태로 앞에서 뽑는다면 BFS구조.
'''
class Solution:
    value = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        q = collections.deque([root])
        sum = 0

        while q:
            node = q.popleft()
            if node:
                if node.val > low:
                    q.append(node.left)
                if node.val < high:
                    q.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum