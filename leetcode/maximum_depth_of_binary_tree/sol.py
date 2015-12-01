# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Recursive solution. Max of max-depth of children plus 1 is the answer.
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        else:
            return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))
