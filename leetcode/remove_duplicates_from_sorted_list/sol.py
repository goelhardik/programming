# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None):
            return None
        pivot = head
        p = head.next
        while (p != None):
            while (p != None and p.val == pivot.val):
                p = p.next
            pivot.next = p
            pivot = p
            
        return head
