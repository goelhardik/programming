# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (head == None):
            return None
        p = head
        l = 0
        tail = None
        # find the length of list; find the tail pointer for later use
        while (p != None):
            tail = p
            p = p.next
            l += 1
            
        # update k for rotation values greater than length
        k = k % l
        if (k == 0):
            return head     # nothing to be done
            
        pp = None   # to find the new tail
        p = head
        count = l
        # go to the correct pointers
        while (count > k):
            pp = p
            p = p.next
            count -= 1
           
        # update pointers 
        if (pp != None):
            tail.next = head
            pp.next = None
            head = p
            
        return head
