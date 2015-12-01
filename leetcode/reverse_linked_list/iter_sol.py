# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        prev = None
        pprev = None
        while (p != None):
            pprev = prev
            prev = p
            p = p.next
            prev.next = pprev
            
        return prev
