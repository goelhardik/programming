"""
Use the first string as pivot.
Iterate over ith character in all the strings until a mismatch is found or some 
string falls short of length.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 0):
            return ""
        flag = 0
        i = 0
        while (1):
            if (i + 1 > len(strs[0])):  # check if first string is short
                flag = 1
                break
            pivot = strs[0][i]
            for j in range(1, len(strs)):
                if (len(strs[j]) < i + 1):  # if string falls short
                    flag = 1
                    break
                if (strs[j][i] != pivot):   # character mismatch
                    flag = 1
                    break
            if (flag == 1):
                break
            i += 1
            
        return strs[0][:i]
