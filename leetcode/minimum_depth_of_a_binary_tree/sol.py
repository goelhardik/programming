# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        else:
            return self._minDepth(root)
            
    def _minDepth(self, root):
        # this condition will be hit only for non-leaf nodes with a null child
        if (root == None):
            return float("inf")

        # if leaf node, return depth = 1
        if (root.left == None and root.right == None):
            return 1
        ldepth = self._minDepth(root.left)
        rdepth = self._minDepth(root.right)
        return (1 + min(ldepth, rdepth))
