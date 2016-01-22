class Solution(object):
    def fractionToDecimal(self, num, den):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        denominator = abs(den)
        numerator = abs(num)
        first = str(numerator // denominator)   # integer part
        if ((num < 0 and den > 0) or (num > 0 and den < 0)):
            first = "-" + first     # add minus sign if required
            
        fraction = numerator % denominator
        if (fraction == 0):
            return first    # if integer answer, return here
        
        decimal = []
        remainders = []
        rec_start = -1
        while (1): 
            if (fraction == 0):     # terminating decimal
                break
            if (fraction in remainders):
                rec_start = remainders.index(fraction)      # if the same remainder is encountered again, it is a recurring decimal
                break
            remainders.append(fraction)
            fraction *= 10
            if (fraction >= denominator):
                decimal.append(str(fraction // denominator))    # append the fractional digit
                fraction %= denominator
            else:
                decimal.append('0')     # append 0 when required
               
        
        
        if (rec_start < 0):
            ans = first + "." + "".join(decimal)
        else:
            ans = first + "." + "".join(decimal[0 : rec_start]) + "(" + "".join(decimal[rec_start : ]) + ")"
            
        return ans
