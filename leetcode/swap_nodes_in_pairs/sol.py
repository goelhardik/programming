# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # nothing to reverse
        if (head == None):
            return None
        p = head
        # nothing to reverse
        if (p.next == None):
            return p
        # update head, reverse the rest of the list and point next of tail to its head
        head = p.next
        p.next = self.swapPairs(head.next)
        head.next = p
        return head
