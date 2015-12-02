# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ans = self._isBalanced(root)
        if (ans < 0):
            return False
        else:
            return True
            
    """
    Recursive implementation.
    Use the return value to return the depth instead of calculating it for each
    node again and again. To detect imbalance, return a negative value.
    """
    def _isBalanced(self, root):
        if (root == None):
            return 0
        left = self._isBalanced(root.left)
        if (left == -1):
            return -1
        right = self._isBalanced(root.right)
        if (right == -1):
            return -1
            
        if (abs(left - right) > 1):
            return -1
        else:
            return (1 + max(left, right))
