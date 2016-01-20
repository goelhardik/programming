# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_val_bst(root, -float("inf"), float("inf"))
        
    # anything to the left of root has maximum value as root.val
    # anything to the right of root has minimum value as root.val
    def is_val_bst(self, root, min, max):
        if (root == None):
            return True
        if (root.val <= min or root.val >= max):
            return False
        return (self.is_val_bst(root.left, min, root.val) and
                self.is_val_bst(root.right, root.val, max))
