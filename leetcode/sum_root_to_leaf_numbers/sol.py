# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        if (root == None):
            return 0
        self.find_numbers(root, 0, result)
        # result will contain all root to leaf numbers
        ans = 0
        for i in range(len(result)):
            ans += result[i]
        return ans
        
    def find_numbers(self, root, item, result):
        # if leaf node, add the number to result
        if (root.left == None and root.right == None):
            item = item * 10 + root.val
            result.append(item)
            return
        
        item = item * 10 + root.val
        if (root.left != None):
            self.find_numbers(root.left, item, result)
        if (root.right != None):
            self.find_numbers(root.right, item, result)
