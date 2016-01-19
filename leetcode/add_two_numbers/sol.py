# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        p = l1
        q = l2
        head = None
        while (p != None and q != None):
            sum = p.val + q.val + carry
            carry = sum // 10
            sum %= 10
            node = ListNode(sum)
            if (head == None):
                head = node
                ptr = head
            else:
                ptr.next = node
                ptr = node
            p = p.next
            q = q.next
                
        if (q != None):
            p = q
            
        while (p != None):
            sum = p.val + carry
            carry = sum // 10
            sum %= 10
            node = ListNode(sum)
            if (head == None):
                head = node
                ptr = head
            else:
                ptr.next = node
                ptr = node
            p = p.next
        
        if (carry > 0):
            node = ListNode(carry)
            ptr.next = node
                
        return head
