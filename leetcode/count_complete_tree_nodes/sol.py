# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        left = self.get_left_height(root)
        right = self.get_right_height(root)
        if (left == right):
            return ((1 << (left + 1)) - 1)
        else:
            return (self.countNodes(root.left) + self.countNodes(root.right) + 1)
        
    def get_left_height(self, root):
        p = root
        h = 0
        while (p.left != None):
            p = p.left
            h += 1
        return h
        
    def get_right_height(self, root):
        p = root
        h = 0
        while (p.right != None):
            p = p.right
            h += 1
        return h
