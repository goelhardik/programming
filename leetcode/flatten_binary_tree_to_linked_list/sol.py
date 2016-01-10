# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if (root == None):
            return None
        q = []
        # store a preorder traversal in a queue
        self.preorder(root, q)
        p = q.pop(0)
        # iterate through the queue and make a flattened tree
        while (len(q) > 0):
            p.left = None
            p.right = q.pop(0)
            p = p.right
        p.left = None
        p.right = None
        return
        
    def preorder(self, root, q):
        if (root == None):
            return
        q.append(root)
        self.preorder(root.left, q)
        self.preorder(root.right, q)
