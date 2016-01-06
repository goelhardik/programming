# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Use a recursive method.
Traverse to the center two/one nodes of the linked list and start comparing and 
returning.
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        count = 0
        while (p != None):
            count += 1
            p = p.next
        node, flag = self.is_palin(head, count)
        return flag
        
    def is_palin(self, head, len):
        if (len == 0):
            return None, True
        if (len == 1):
            return head.next, True
        if (len == 2):
            if (head.val == head.next.val):
                return head.next.next, True
            else:
                return None, False
        node, flag = self.is_palin(head.next, len - 2)
        if (node == None):
            return node, flag
        if (head.val == node.val):
            return node.next, True
        else:
            return None, False
