# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None):
            return None
        head = self.sort_list(head)
        return head
        
    def sort_list(self, head):
        if (head.next == None):
            return head
        
        # divide into 2 lists
        f = head
        s = head
        while (f.next != None and f.next.next != None):
            f = f.next.next
            s = s.next
            
        head2 = s.next
        s.next = None
        # sort each list
        h1 = self.sort_list(head)
        h2 = self.sort_list(head2)
        # merge lists
        hfinal = self.merge_lists(h1, h2)
        return hfinal
        
    def merge_lists(self, h1, h2):
        p = h1
        q = h2
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
         
        # set head
        if (h1.val < h2.val):
            hfinal = h1
        else:
            hfinal = h2
            
        return hfinal
