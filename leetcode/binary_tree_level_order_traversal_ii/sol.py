# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import Queue

"""
Use two queues to track each level separately.
"""
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if (root == None):
            return []
        q1 = Queue.Queue()
        q2 = Queue.Queue()
        ans = []
        q1.put(root)
        while (not q1.empty()):
            item = []
            while (not q1.empty()):
                node = q1.get()
                if (node.left != None):
                    q2.put(node.left)
                if (node.right != None):
                    q2.put(node.right)
                item.append(node.val)
            """
            current level is empty, append the current level traversal, move 
            to next level
            """
            ans.insert(0, item)
            q1 = q2
            q2 = Queue.Queue()
            
        return ans
