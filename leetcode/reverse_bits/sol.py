class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        # extract last bit, shift number to the right, insert bit in the result
        for i in range(32):
            bit = n & 1
            n = n >> 1
            ans = ans << 1 | bit
            
        return ans
