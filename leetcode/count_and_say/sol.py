class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        res = ""
        for i in range(1, n):
            pivot = s[0]
            count = 0
            for j in range(len(s)):
                if (s[j] == pivot):
                    count += 1
                else:
                    res += str(count) + pivot
                    pivot = s[j]
                    count = 1
            res += str(count) + pivot
            s = res
            res = ""
            
        return s
