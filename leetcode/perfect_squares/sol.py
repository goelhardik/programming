class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        edges = [i * i for i in range(int(math.floor(math.sqrt(n))), 0, -1)]
        level = 1
        q1 = [0]
        q2 = []
        # use BFS approach to get the solution faster; we stop as soon as a sum is found
        # using BFS gives the minimum number of numbers that sum to n
        while (1):
            while (len(q1) > 0):
                num = q1.pop(0)
                for edge in edges:
                    tmp = num + edge
                    if (tmp == n):
                        return level
                    # prune the search if the sum > n, as it will only increase
                    if (tmp < n):
                        q2.append(tmp)
            level += 1
            q1 = q2
            q2 = []
