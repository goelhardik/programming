"""
Implemented stack using the python list. Used standard stack operations only.
For the size of the stack, len operation is used. It means the same thing 
effectively.
"""
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if (len(self.s2) > 0):
            self.s2.pop()
        else:
            while (len(self.s1) > 0):
                self.s2.append(self.s1.pop())
            self.s2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if (len(self.s1) > 0):
            return self.s1[0]
        else:
            return self.s2[len(self.s2) - 1]

    def empty(self):
        """
        :rtype: bool
        """
        if (len(self.s2) == 0 and len(self.s1) == 0):
            return True
        return False
