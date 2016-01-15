class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = set([])
        subs = set([])
        for i in range(len(s)):
            if (i < 9):
                continue
            substring = s[i - 9 : i + 1]
            if (substring in subs):
                result.add(substring)
            else:
                subs.add(substring)
                
        return list(result)
