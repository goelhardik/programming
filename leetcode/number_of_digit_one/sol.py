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
            index = n // ten    # multiple of current digit (ones/tens/hundreds/...). eg. 5 for n = 56 for tens digit
            mult = ten // 10
            qty = (n % ten - (mult - 1))    # count number of ones in 123 for n = 5123
            if (qty <= 0):
                ans = 0
            elif (qty > mult):
                ans = mult
            else:
                ans = qty
                
            ones += index * mult + ans
            if (index == 0):
                break
            ten *= 10
            
        return ones
