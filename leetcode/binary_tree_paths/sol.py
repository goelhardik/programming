# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        item = []
        self.return_paths(root, result, item)
        return result
        
    def return_paths(self, root, result, item):
        if (root == None):
            return
        # if it is a leaf node, append the node's val and add to the output
        if (root.left == None and root.right == None):
            item.append(str(root.val))
            result.append("->".join(list(item)))
            item.pop()
            return
        # if not a leaf node, recurse on children
        item.append(str(root.val))
        if (root.left != None):
            self.return_paths(root.left, result, item)
        if (root.right != None):
            self.return_paths(root.right, result, item)
        item.pop()
