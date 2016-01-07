# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.arrayToBST(0, len(nums) - 1, nums)
        
    def arrayToBST(self, low, high, nums):
        if (low > high):
            return None
        
        mid = low + (high - low) // 2
        root = TreeNode(nums[mid])
        root.left = self.arrayToBST(low, mid - 1, nums)
        root.right = self.arrayToBST(mid + 1, high, nums)
        return root
