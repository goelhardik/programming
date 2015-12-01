"""
Iterate over each digit, adding them; repeat until sum < 9
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while (num > 9):
            sum = 0
            while (num > 0):
                sum += num % 10
                num = num // 10
            num = sum
        return num
