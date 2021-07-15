# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# My Solution
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
    ''' 좀 더 압축한 코드
    결국, 재귀의 의미는 리프노드 까지 내려갔다가 부모 노드로 복귀할 때 root를 반환하지만 
         해당 root가 인자로 들어온 반대 방향으로 간다는 점이 포인트이다.
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root, right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    return None
    '''

# BFS 코드 -> DFS로 바꾸려면 그저 pop으로 뒤에서 꺼내기만 하면된다.
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = collections.deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left

                q.append(node.left)
                q.append(node.right)
