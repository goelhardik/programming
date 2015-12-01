# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if (root == None):
            return None
        # swap the left and right children of the root
        tmp = root.left
        root.left = root.right
        root.right = tmp
        # call invertTree recursively for each child of the root
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
