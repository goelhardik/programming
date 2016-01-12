# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.bt(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)
        
    def bt(self, inorder, li, hi, postorder, lp, hp):
        if (li > hi):
            return None
        # last element of postorder is the root
        root = TreeNode(postorder[hp])
        # find index of root in the inorder traversal
        root_ind = inorder.index(postorder[hp])
        # left subtree will contain all inorder elements to left of root
        root.left = self.bt(inorder, li, root_ind - 1, postorder, lp, lp + (root_ind - li) - 1)
        # right subtree will contain all inorder elements to right of root
        root.right = self.bt(inorder, root_ind + 1, hi, postorder, lp + (root_ind - li), hp - 1)
        return root
