class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # only the bulbs which have odd number of divisors from 1 to the number itself, will remain on
        # thus we need to find the number of perfect squares between 1 and n
        return int(math.floor(math.sqrt(n)))
