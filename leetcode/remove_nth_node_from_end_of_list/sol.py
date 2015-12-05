# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if (head == None or n == 0):
            return head
        p = head
        count = 0
        # get a difference of n between two pointers
        while (count < n):
            count += 1
            p = p.next
        q = head
        pq = None   # previous pointer to enable deleting the node
        while (p != None):
            p = p.next
            pq = q
            q = q.next
        # if head is the node to be deleted
        if (pq == None):
            head = head.next
        else:
            pq.next = q.next
            
        return head
