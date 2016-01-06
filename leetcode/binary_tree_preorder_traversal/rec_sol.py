# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self._preorder(root, result)
        return result
        
    def _preorder(self, root, result):
        if (root == None):
            return
        result.append(root.val)
        self._preorder(root.left, result)
        self._preorder(root.right, result)
