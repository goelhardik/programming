# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        if (root == None):
            return result
        self.find_paths(root, [], 0, sum, result)
        return result
        
    def find_paths(self, root, item, sum, target, result):
        # if leaf node, then add the answer if sum matches
        if (root.left == None and root.right == None):
            item.append(root.val)
            sum += root.val
            if (sum == target):
                result.append(list(item))
            item.pop()
            return
        
        item.append(root.val)
        sum += root.val
        if (root.left != None):
            self.find_paths(root.left, item, sum, target, result)
        if (root.right != None):
            self.find_paths(root.right, item, sum, target, result)
        item.pop()
