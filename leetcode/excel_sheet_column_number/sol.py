class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s) - 1, -1, -1):
            val = ord(s[i]) - ord('A') + 1
            sum += val * (26 ** (len(s) - 1 - i))
            
        return sum
