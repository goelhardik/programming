class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend == -2147483648 and divisor == -1):
            return 2147483647
        count = 0
        pdivd = abs(dividend)
        pdivs = abs(divisor)
        while (pdivd >= pdivs):
            shift = 0
            while (pdivd >= (pdivs << shift)):
                shift += 1
            count += 1 << (shift - 1)
            pdivd -= pdivs << (shift - 1)
            
        if ((dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)):
            count = -count
        return count
