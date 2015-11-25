class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self._sqrt(x, 0, x)
        
    """
    A binary search approach is used.
    """
    def _sqrt(self, target, start, end):
        mid = (start + end) / 2
        num = mid * mid
        if (num == target):
            ans = mid
        elif (num > target and (mid - 1) * (mid - 1) < target):
            ans = mid - 1
        elif (num > target):
            ans = self._sqrt(target, start, mid)
        else:
            ans = self._sqrt(target, mid + 1, end)
        return ans
