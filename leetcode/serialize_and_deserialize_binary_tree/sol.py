# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # use preorder traversal to serialize tree; use # to denote null nodes
    def _serialize(self, root, result):
        if (root == None):
            result.append(str("#"))
            return
        result.append(str(root.val))
        self._serialize(root.left, result)
        self._serialize(root.right, result)
        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        self._serialize(root, result)
        return ".".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(".")
        root, waste = self._deserialize(data, 0)
        return root
        
    def _deserialize(self, data, i):
        if (i >= len(data) or data[i] == "#"):
            return None, i
            
        root = TreeNode(data[i])
        root.left, i = self._deserialize(data, i + 1)
        root.right, i = self._deserialize(data, i + 1)
        return root, i

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

