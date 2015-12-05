# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Find the length of both the lists. Move to that node in the bigger list, 
starting from which the length of both the lists is same.
Start moving a pointer each from here and return when the pointer becomes same.
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (headA == None or headB == None):
            return None
            
        l1 = self.find_len(headA)
        l2 = self.find_len(headB)
        if (l1 > l2):
            big = headA
            small = headB
        else:
            big = headB
            small = headA
        diff = abs(l1 - l2)
        p = big
        q = small

        # move pointer to correct position in the bigger list
        for i in range(diff):
            p = p.next

        # now find the intersection if any
        while (p != None and q != None and p != q):
            p = p.next
            q = q.next
        if (p == None or q == None):
            return None
        else:
            return p # or q
            
    def find_len(self, head):
        count = 0
        p = head
        while (p != None):
            count += 1
            p = p.next
            
        return count
