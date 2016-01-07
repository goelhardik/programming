# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        # parent linked list pointers
        phead = None
        pcurr = None
        # child linked list pointers
        chead = root
        ccurr = root
        while (chead != None):
            if (pcurr == None):
                ccurr.next = None
                phead = chead
                pcurr = chead
                chead = chead.left
                ccurr = chead
            elif (ccurr == pcurr.left):
                ccurr.next = pcurr.right
                ccurr = ccurr.next
            elif (ccurr == pcurr.right):
                pcurr = pcurr.next
            else:
                ccurr.next = pcurr.left
                ccurr = ccurr.next
