# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = collections.deque()
        q.append(root)
        ret = ['#']
        while q:
            node = q.popleft()
            if node:
                ret.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                ret.append('#')
        return ' '.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '# #':
            return None
        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        q = collections.deque([root])
        index = 2
        while q:
            node = q.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))