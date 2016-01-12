# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.bt(inorder, 0, len(inorder) - 1, preorder, 0, len(preorder) - 1)
        
    def bt(self, inorder, li, hi, preorder, lp, hp):
        if (li > hi):
            return None
        # first element of preorder is the root
        root = TreeNode(preorder[lp])
        # find index of root in the inorder traversal
        root_ind = inorder.index(preorder[lp])
        # left subtree will contain all inorder elements to left of root
        root.left = self.bt(inorder, li, root_ind - 1, preorder, lp + 1, lp + (root_ind - li))
        # right subtree will contain all inorder elements to right of root
        root.right = self.bt(inorder, root_ind + 1, hi, preorder, lp + (root_ind - li) + 1, hp)
        return root
