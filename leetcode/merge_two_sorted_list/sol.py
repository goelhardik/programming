# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # check for base null conditions
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        p = l1
        pp = None   # previous pointer for first list
        q = l2
        qq = None   # previous pointer for second list
        # set the head for the new list
        if (p.val < q.val):
            head = p
        else:
            head = q
        while (p != None and q != None):
            if (p.val < q.val):
                while (p != None and p.val < q.val):
                    pp = p
                    p = p.next
                pp.next = q
            else:
                while (q != None and q.val <= p.val):
                    qq = q
                    q = q.next
                qq.next = p
                
        return head
