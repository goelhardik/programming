"""
Maintain a hash map of the numbers seen. If a number is seen again during the 
loop, then it is a cycle.
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        map = {}
        map[n] = 1
        while (n != 1):
            sum = 0
            while (n > 0):
                sum += (n % 10) ** 2
                n //= 10
            n = sum
            if (n not in map):
                map[n] = 1
            else:
                return False
                
        return True
