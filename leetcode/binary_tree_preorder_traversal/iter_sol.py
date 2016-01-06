# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        p = root
        while (p != None or len(stack) != 0):
            # if the left child is not found, use the first right child stored in the stack
            if (p == None):
                p = stack.pop()
            else:
                # use a stack to store the right children
                if (p.right != None):
                    stack.append(p.right)
                result.append(p.val)
                p = p.left
                
        return result
