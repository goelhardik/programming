class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if (len(words) != len(pattern)):
            return False
        map = {}
        for i in range(len(pattern)):
            if (pattern[i] not in map.keys()):
                if (words[i] in map.values()):
                    return False
                else:
                    map[pattern[i]] = words[i]
            else:
                if (map[pattern[i]] != words[i]):
                    return False
                    
        return True
