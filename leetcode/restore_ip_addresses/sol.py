class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if (n < 4 or n > 12):
            return []
            
        result = []
        self.find_ips(s, 0, result, [])
        return result
        
    def find_ips(self, s, start, result, item):
        # base conditions
        if (len(item) > 4):
            return
        if (start == len(s)):
            if (len(item) == 4):
                result.append(".".join(list(item)))
                return
            else:
                return
            
        # try all possible lengths : 1, 2, 3
        for i in range(1, min(4, len(s) - start + 1)):
            # skip numbers that start with 0 and are non-zero
            # also skip zero numbers having multiple zeros
            if (i > 1 and s[start] == "0"):
                continue
            # skip numbers bigger than 255
            if (i == 3 and int(s[start : start + i]) > 255):
                continue
            item.append(s[start : start + i])
            self.find_ips(s, start + i, result, item)
            item.pop()
