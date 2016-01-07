# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self._inorder(root, result)
        return result
        
    def _inorder(self, root, result):
        if (root == None):
            return
        self._inorder(root.left, result)
        result.append(root.val)
        self._inorder(root.right, result)
