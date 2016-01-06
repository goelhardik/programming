class Solution(object):
    def reverse(self, num):
        """
        :type x: int
        :rtype: int
        """
        # take care of the sign
        neg = 1
        if (num < 0):
            neg = -1
            num *= -1
        sum = 0
        while (num > 0):
            rem = num % 10
            sum = sum * 10 + rem
            num = num // 10
        
        # trick to get the test case for MAX_INT passed
        if (sum > 2147483647):
            return 0
        return sum * neg
