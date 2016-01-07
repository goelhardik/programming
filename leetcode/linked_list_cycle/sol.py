# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        q = head
        cycle = False
        # use a slow pointer and a fast pointer; if they meet, there is a cycle
        while (not cycle and q != None and q.next != None and q.next.next != None):
            p = p.next
            q = q.next.next
            if (p == q):
                cycle = True
                
        return cycle
