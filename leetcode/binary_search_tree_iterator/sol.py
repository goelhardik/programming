# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        p = root
        self.stack = []
        while (p != None):
            self.stack.append(p)
            p = p.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return (len(self.stack) > 0)

    def next(self):
        """
        :rtype: int
        """
        if (len(self.stack) > 0):
            p = self.stack.pop()
            tmp = p.val
            p = p.right
            while (p != None):
                self.stack.append(p)
                p = p.left
                
            return tmp

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
