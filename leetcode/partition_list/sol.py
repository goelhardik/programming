# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        pq = None
        pp = None
        p = head
        while (p != None):
            # keep going until an out of place element is found
            if (p.val < x):
                pp = p
                p = p.next
            else:
                q = p
                pq = pp
                # find the next correct element to be placed before x
                while (q != None and q.val >= x):
                    pq = q
                    q = q.next
                # the partition is done
                if (q == None):
                    break
                # delete q from its place and insert before p; update head if needed
                if (pp != None):
                    pp.next = q
                else:
                    head = q
                pq.next = q.next
                q.next = p
                pp = q
                q = pq.next
                
        return head
