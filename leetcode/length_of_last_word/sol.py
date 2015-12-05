class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # start from the back, that's optimal
        i = len(s) - 1
        count = 0
        while (i >= 0):
            if (s[i] == ' '):
                if (count == 0):
                    pass
                else:
                    return count
            else:
                count += 1
            i -= 1
            
        return count
