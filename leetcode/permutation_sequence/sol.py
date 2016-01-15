class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        digits = [str(i) for i in range(1, n + 1)]
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        res = []
        """
        For n digits, 1st digit changes after n!/n permutations; that is
        after (n - 1)! permutations. So find out how many times the first digit
        has changed by doing k/(n - 1)!. Append the corresponding digit.
        Now we are left with (n - 1) digits and we need to find (k % (n - 1)!)th
        permutation. So repeat the above.
        """
        for i in range(n, 1, -1):
            fact //= i
            ind = k // fact
            res.append(digits[ind])
            del digits[ind]
            k %= fact
            
        res.append(digits[0])
        return "".join(res)
