# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Iterate from the given node till the end of the list, copying the data from the 
next node to the current node. Delete the last node.
"""
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = None
        while (node.next != None):
            prev = node
            node.val = node.next.val
            node = node.next
        prev.next = None
