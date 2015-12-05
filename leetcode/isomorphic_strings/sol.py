class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False
        map = {}
        for i in range(len(s)):
            if (s[i] not in map):
                map[s[i]] = t[i]
            else:
                if (map[s[i]] != t[i]):
                    return False
        map = {}
        for i in range(len(t)):
            if (t[i] not in map):
                map[t[i]] = s[i]
            else:
                if (map[t[i]] != s[i]):
                    return False
                    
        return True
