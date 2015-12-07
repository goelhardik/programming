# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pp = None
        p = head
        while (p != None):
            # move forward if node not to be deleted
            if (p.val != val):
                pp = p
                p = p.next
            else:   # node to be deleted
                if (pp == None):    # handle deletion of head
                    head = p.next
                    p = head
                else:   # delete non-head node
                    pp.next = p.next
                    p = p.next
                    
        return head
