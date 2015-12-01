# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # a node can be a descendant of itself
        if (root == p or root == q):
            return root
            
        # if the given nodes lie on the opposite side of root, root is the LCA
        if ((p.val < root.val and q.val > root.val) or (q.val < root.val and p.val > root.val)):
            return root
        # else move to the correct side of the root and make a recursive call
        elif (p.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
