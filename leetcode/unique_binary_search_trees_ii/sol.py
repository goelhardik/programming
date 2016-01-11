# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if (n == 0):
            return []
        return self.find_trees(1, n)
        
    def find_trees(self, low, high):
        if (low > high):
            return [None]
        trees = []
        for i in range(low, high + 1):
            # find all possible left children
            left = self.find_trees(low, i - 1)
            # right children
            right = self.find_trees(i + 1, high)
            # combine children in all possible ways
            for (l, r) in itertools.product(left, right):
                node = TreeNode(i)
                node.left = l
                node.right = r
                trees.append(node)
                
        return trees
