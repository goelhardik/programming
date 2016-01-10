# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q1 = []
        q2 = []
        result = []
        if (root == None):
            return result
        q1.append(root)
        # do BFS; store the last node at each level
        while (len(q1) > 0):
            while (len(q1) > 0):
                p = q1.pop(0)
                if (p.left != None):
                    q2.append(p.left)
                if (p.right != None):
                    q2.append(p.right)
                    
            result.append(p.val)
            q1 = q2
            q2 = []
            
        return result
