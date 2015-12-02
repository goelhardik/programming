# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if (root == None):
            return []
        q1 = Queue.Queue()
        q2 = Queue.Queue()
        q1.put(root)
        ans = []
        while (not q1.empty()):
            item = []
            while (not q1.empty()):
                node = q1.get()
                if (node.left != None):
                    q2.put(node.left)
                if (node.right != None):
                    q2.put(node.right)
                item.append(node.val)
            ans.append(item)
            q1 = q2
            q2 = Queue.Queue()
            
        return ans
