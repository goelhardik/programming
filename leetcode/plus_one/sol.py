class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        if (l == 0):
            return [1]
        sum = digits[l - 1] + 1
        carry = sum // 10
        digits[l - 1] = sum % 10
        if (carry < 1):
            return digits
        for i in range(l - 2, -1, -1):
            sum = digits[i] + carry
            carry = sum // 10
            digits[i] = sum % 10
            if (carry < 1):
                break
            
        if (carry > 0):
            digits.insert(0, 1)
        return digits
