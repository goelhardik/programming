# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pp = None
        p = head
        count = 1
        while (p != None):
            if (count == m):
                break
            pp = p
            p = p.next
            count += 1
            
        # store mth node
        head_m = p
        # store the node previous to mth node
        prev_m = pp
        # start reversing list from mth node
        ptr = p.next
        while (count <= n):
            p.next = pp
            pp = p
            p = ptr
            if (ptr != None):
                ptr = ptr.next
            count += 1
        
        # update head if required
        if (prev_m == None):
            head = pp
        else:
            prev_m.next = pp
        head_m.next = p
        return head
