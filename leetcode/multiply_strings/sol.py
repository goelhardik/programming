class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        res = [0 for i in range(l1 + l2)]
        for i in range(l1):
            for j in range(l2):
                res[(l1 - i - 1) + (l2 - j - 1)] += int(num1[i]) * int(num2[j])
                
        ans = ""
        carry = 0
        for i in range(len(res)):
            sum = res[i] + carry
            digit = sum % 10
            carry = sum // 10
            ans = str(digit) + ans
            
        # remove leading zeros
        ind = 0
        for i in range(len(ans)):
            if (ans[i] == "0"):
                ind += 1
            else:
                break
        ans = ans[ind :]
        
        if (len(ans) == 0):
            ans = "0"
        return ans
