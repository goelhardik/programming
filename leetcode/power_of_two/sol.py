"""
Keep right shifting by 1 bit until bit 0 becomes 1. Check if the number is still 
not equal to 1, then it is not a power of 2; else it is.
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n == 0):
            return False
        while (1):
            if (n % 2 == 0):
                n = n >> 1
            elif (n != 1):
                return False
            else:
                return True
