class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n <= 0):
            return 0
        ones = 0
        ten = 10
        while (1):
            qty = (n % ten - (ten // 10 - 1))
            if (qty <= 0):
                ans = 0
            elif (qty > ten // 10):
                ans = ten // 10
            else:
                ans = qty
                
            ones += (n // ten) * (ten // 10) + ans
            if (n // ten == 0):
                break
            ten *= 10
            
        return ones
