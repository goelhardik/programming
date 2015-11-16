class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        matrix = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            matrix[i][i] = 1
            
        max = 1
        start = 0
        """
        Use DP to find the longest palindrome. s[i...j] is a palindrome if
        s[i] == s[j] and s[i+1....j-1] is a palindrome.
        """
        for d in range(1, len(s)):
            count = 0
            for i in range(len(s) - d):
                j = i + d
                if (s[i] == s[j]):
                    matrix[i][j] = 1
                    if (i + 1 <= j - 1 and matrix[i + 1][j - 1] == 0):
                        matrix[i][j] = 0
                if (matrix[i][j] == 1):
                    count += 1
                    if (j - i + 1 > max):
                        max = j - i + 1
                        start = i
                        
            if (count == 0):    # some optimization; break if no palindrome of length d
                break
            
        return s[start : start + max]
