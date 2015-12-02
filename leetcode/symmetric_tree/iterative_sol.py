# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Use two queues, one each to store the children of the left and right children of 
the current nodes.
"""
import Queue

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root == None):
            return True
        if (root.left == None and root.right == None):
            return True
        elif (root.left == None or root.right == None):
            return False
        q1 = Queue.Queue()
        q2 = Queue.Queue()
        q1.put(root.left)
        q2.put(root.right)
        while (not q1.empty() and not q2.empty()):
            first = q1.get()
            second = q2.get()
            if (first.val != second.val):
                return False
            # push the left of first and right of second together
            if (first.left == None and second.right == None):
                pass
            elif (first.left == None or second.right == None):
                return False
            else:
                q1.put(first.left)
                q2.put(second.right)
            # push the right of first and left of second together
            if (first.right == None and second.left == None):
                pass
            elif (first.right == None or second.left == None):
                return False
            else:
                q1.put(first.right)
                q2.put(second.left)
                
        if (q1.empty() and q2.empty()):
            return True
        else:
            return False
