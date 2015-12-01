"""
Sum of digits of a number is the same as the remainder on dividing the number by 
9; except in the case of multiples of 9. Handle those separately.
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if (num == 0):
            return 0
        if (num % 9 != 0):
            return num % 9
        else:
            return 9
