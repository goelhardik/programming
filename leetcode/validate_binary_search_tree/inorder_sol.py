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
        tree = []
        self.inorder_traversal(root, tree)
        for i in range(1, len(tree)):
            if (tree[i] <= tree[i - 1]):
                return False
                
        return True
        
    def inorder_traversal(self, root, tree):
        if (root == None):
            return
        self.inorder_traversal(root.left, tree)
        tree.append(root.val)
        self.inorder_traversal(root.right, tree)
