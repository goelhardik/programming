class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (num <= 0):
            return False
        while (num > 1):
            if (num % 5 == 0):
                num //= 5
            elif (num % 3 == 0):
                num //= 3
            elif (num % 2 == 0):
                num //= 2
            elif (num > 1):
                return False
                
        return True