# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if (root == None):
            return False
        else:
            return self._hasPathSum(root, sum)
        
    def _hasPathSum(self, root, sum):
        sum -= root.val
        # if root is leaf node, return
        if (root.left == None and root.right == None):
            if (sum == 0):
                return True
            else:
                return False
                
        if (root.left != None):
            if (self._hasPathSum(root.left, sum)):
                return True
        if (root.right != None):
            if (self._hasPathSum(root.right, sum)):
                return True
                
        return False
