class Solution(object):
    def convertToTitle(self, num):
        """
        :type n: int
        :rtype: str
        """
        out = ""
        # start from the end and generate the front
        while (num > 26):
            rem = num % 26
            # take care of 'Z'
            if (rem == 0):
                rem = 26
                num -= 1
            c = chr(rem + ord("A") - 1)
            out = str(c) + out
            num = num // 26
            
        if (num > 0):
            out = str(chr(num + ord("A") - 1)) + out
            
        return out
