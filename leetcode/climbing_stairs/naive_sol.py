"""
Keep increasing the count of double steps, calculate the number of ways and add 
them to the total ways count. Use factorial to calculate the number of ways.
Very naive solution.
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = n
        twos = 0
        count = 1
        for i in range(n // 2):
            twos += 1
            ones -= 2
            count += self.fact(twos + ones) // (self.fact(twos) * self.fact(ones))
            
        return count
        
    def fact(self, n):
        prod = 1
        while (n > 0):
            prod *= n
            n -= 1
            
        return prod
