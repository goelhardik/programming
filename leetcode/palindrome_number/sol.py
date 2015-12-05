class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        sum = 0
        orig = x
        while (x > 0):
            rem = x % 10
            sum = sum * 10 + rem
            x = x // 10
        if (orig == sum):
            return True
        else:
            return False
