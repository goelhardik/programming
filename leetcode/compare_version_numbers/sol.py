class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ans = 0
        v1 = version1.split(".")
        v2 = version2.split(".")
        l1 = len(v1)
        l2 = len(v2)
        for i in range(min(l1, l2)):
            if (int(v1[i]) > int(v2[i])):
                ans = 1
                break
            elif (int(v1[i]) < int(v2[i])):
                ans = -1
                break
        if (ans != 0):
            return ans

        if (l1 == l2):
            return ans
        elif (l1 > l2):
            for i in range(l2, l1):
                if (int(v1[i]) > 0):
                    ans = 1
                    break
        elif (l1 < l2):
            for i in range(l1, l2):
                if (int(v2[i]) > 0):
                    ans = -1
                    break
                
        return ans
