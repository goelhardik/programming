# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = head
        f = head
        cycle = 0
        while (f != None and f.next != None and f.next.next != None):
            f = f.next.next
            s = s.next
            if (f == s):
                cycle = 1
                break
        if (cycle == 0):
            return None
            
        p = head
        while (p != s):
            p = p.next
            s = s.next
            
        return p
