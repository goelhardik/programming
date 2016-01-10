# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        p = head
        while (p != None and p.next != None):
            p = p.next
        tail = p
        return self.convert(head, tail)
        
    def convert(self, head, tail):
        if (head == None or tail == None):
            return None
        if (head == tail):
            x = TreeNode(head.val)
            return x
            
        # find middle
        f = head
        s = head
        # ps will be the node preceeding s; and None if s is the head
        ps = None
        while (f != tail and f.next != tail):
            f = f.next.next
            ps = s
            s = s.next
            
        # s is the middle node  
        root = TreeNode(s.val)
        root.left = self.convert(head, ps)
        root.right = self.convert(s.next, tail)
        return root
