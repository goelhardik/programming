# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = 0
        p = root
        stack = []
        while (p != None or len(stack) > 0):
            if (p != None):
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                count += 1
                if (count == k):
                    return p.val
                p = p.right
