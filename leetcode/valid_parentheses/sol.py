class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = ['(', '[', '{']
        close = [')', ']', '}']
        stack = []
        for i in range(len(s)):
            if (s[i] in open):
                stack.append(open.index(s[i]))
            elif (s[i] in close):
                if (len(stack) == 0):
                    return False
                top = stack.pop()
                if (top != close.index(s[i])):
                    return False
                    
        if (len(stack) != 0):
            return False
        else:
            return True
