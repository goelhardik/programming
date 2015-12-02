class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count the powers of 5 in the number factorial
        i = 1
        count = 0
        while (n // (5 ** i) > 0):
            count += n // (5 ** i)
            i += 1
            
        return count
