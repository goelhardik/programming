class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if (len(a) < len(b)):
            tmp = a
            a = b
            b = tmp
        carry = 0
        res = ""
        for i, j in zip(range(len(a) - 1, -1, -1), range(len(b) - 1, -1, -1)):
            sum = int(a[i]) + int(b[j]) + carry
            carry = sum // 2
            sum %= 2
            res += str(sum)
        if (len(res) < len(a)):
            for i in range(len(a) - len(res) - 1, -1, -1):
                sum = int(a[i]) + carry
                carry = sum // 2
                sum %= 2
                res += str(sum)
        if (carry > 0):
            res += str(carry)
        res = self.reverse_string(res)
        return res
        
    def reverse_string(self, res):
        ans = ""
        for i in range(len(res)):
            ans += res[len(res) - i - 1]
            
        return ans
