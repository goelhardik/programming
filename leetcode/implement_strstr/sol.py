class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        if (n == 0):
            return 0
        for i in range(len(haystack)):
            if (i + n > len(haystack)):
                break
            if (haystack[i : i + n] == needle):
                return i
                
        return -1
