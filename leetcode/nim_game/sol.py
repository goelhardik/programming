"""
By observation, if the number of stones is a multiple of 4, you cannot win the 
game.
"""
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n == 0):
            return True
        if (n % 4 == 0):
            return False
        else:
            return True
