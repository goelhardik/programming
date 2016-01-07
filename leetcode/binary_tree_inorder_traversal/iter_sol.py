# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        p = root
        while (p != None or len(stack) != 0):
            if (p == None):
                p = stack.pop()
                result.append(p.val)
                p = p.right
            else:
                stack.append(p)
                p = p.left
                
        return result
