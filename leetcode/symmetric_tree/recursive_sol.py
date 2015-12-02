# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root == None):
            return True
        else:
            return self._isSymmetric(root.left, root.right)
            
    # conditions are self-explanatory
    def _isSymmetric(self, p, q):
        if (p == None and q == None):
            return True
        elif (p == None or q == None):
            return False
        elif (p.val != q.val):
            return False
        else:
            return (self._isSymmetric(p.left, q.right) and self._isSymmetric(p.right, q.left))
