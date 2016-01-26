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
        phead = None
        pcurr = None
        chead = root
        ccurr = root
        while (chead != None):
            if (pcurr == None):
                ccurr.next = None   # last node at this level
                # find next chead
                phead = chead
                pcurr = phead
                chead = phead.left
                ccurr = chead
                while (chead == None and phead != None):
                    if (phead.right != None):
                        chead = phead.right
                        ccurr = chead
                    else:
                        phead = phead.next
                        pcurr = phead
                        if (phead == None):
                            break
                        chead = phead.left
                        ccurr = chead
            elif (ccurr == pcurr.left):
                if (pcurr.right != None):
                    ccurr.next = pcurr.right
                    ccurr = ccurr.next
                else:
                    pcurr = pcurr.next
            elif (ccurr == pcurr.right):
                pcurr = pcurr.next
            else:
                if (pcurr.left != None):
                    ccurr.next = pcurr.left
                    ccurr = ccurr.next
                elif (pcurr.right != None):
                    ccurr.next = pcurr.right
                    ccurr = ccurr.next
                else:
                    pcurr = pcurr.next
