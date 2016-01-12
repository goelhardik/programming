# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # use two stacks to do level order traversal
        s1 = []
        s2 = []
        result = []
        if (root == None):
            return result
        # switch the order of children at each level
        count = 1
        s1.append(root)
        while (len(s1) > 0):
            item = []
            while (len(s1) > 0):
                node = s1.pop()
                item.append(node.val)
                if (count % 2 != 0):
                    if (node.left != None):
                        s2.append(node.left)
                    if (node.right != None):
                        s2.append(node.right)
                else:
                    if (node.right != None):
                        s2.append(node.right)
                    if (node.left != None):
                        s2.append(node.left)
                        
            s1 = s2
            s2 = []
            result.append(list(item))
            count += 1
            
        return result
