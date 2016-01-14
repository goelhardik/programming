class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        uglies = []
        uglies.append(1)
        i2 = 0
        i3 = 0
        i5 = 0
        while (count < n):
            # next multiples of 2, 3, 5 to be considered
            mult2 = uglies[i2] * 2
            mult3 = uglies[i3] * 3
            mult5 = uglies[i5] * 5
            # take the minimum multiple, and update the index of respective primes
            next_ugly = min(mult2, mult3, mult5)
            if (next_ugly == mult2):
                i2 += 1
            if (next_ugly == mult3):
                i3 += 1
            if (next_ugly == mult5):
                i5 += 1
                
            count += 1
            uglies.append(next_ugly)
            
        return uglies[n - 1]
