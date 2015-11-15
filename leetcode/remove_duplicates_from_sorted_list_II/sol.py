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
        prev = None
        p = head
        pivot = head
        while (p != None):
            while (p != None and p.val == pivot.val):
                p = p.next
            if (pivot.next == p):   # no deletion
                prev = pivot
            else:                   # duplicate detected
                if (prev == None):  # update head if first node has a duplicate
                    head = p
                else:
                    prev.next = p
            pivot = p
                    
        return head
