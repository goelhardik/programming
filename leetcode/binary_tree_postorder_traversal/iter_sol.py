# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        p = root
        ans = []
        while (p != None or stack):
            if (p == None):
                p = stack.pop()
            else:
                if (p.left != None):
                    stack.append(p.left)
                ans.append(p.val)
                p = p.right
                 
        self.reverse_list(ans)   
        return ans
        
    def reverse_list(self, ans):
        i = 0
        j = len(ans) - 1
        while (i < j):
            ans[i], ans[j] = ans[j], ans[i]
            i += 1
            j -= 1
