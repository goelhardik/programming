class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = (x >> 1) + 1
        while (low <= high):
            mid = (low + high) >> 1
            sq = mid * mid
            if (sq <= x and ((mid + 1) * (mid + 1) > x)):
                return mid
            elif (sq > x):
                high = mid - 1
            else:
                low = mid + 1
