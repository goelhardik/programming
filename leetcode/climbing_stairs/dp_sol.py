"""
Identify that this is a DP problem. For reaching the nth stair, we can either 
come from (n - 2)th stair or the (n - 1)th stair.
Hence the total number of ways for the nth stair can be obtained by a bottom-up 
DP solution.
It works like a Fibonacci sequence.
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n <= 2):
            return n
        ways = [0 for i in range(3)]
        ways[0] = 1
        ways[1] = 2
        for i in range(2, n):
            ways[2] = ways[0] + ways[1]
            ways[0] = ways[1]
            ways[1] = ways[2]
            
        return ways[2]
