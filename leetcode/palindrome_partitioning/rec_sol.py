class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = self._partition(s, 0, len(s) - 1)
        return result
        
    def _partition(self, s, low, high):
        if (low > high):
            return [[]]
            
        result = []
        # consider all the lengths for the first substring
        for l in range(1, high - low + 2):
            if (not self.is_palin(s[low : low + l])):
                continue
            else:
                # whenever the first substring is a palindrome, calculate partitions of the rest of the string
                rest = self._partition(s, low + l, high)
                # append the first substring to each partition of the rest of the string
                for partition in rest:
                    partition.insert(0, s[low : low + l])
                    result.append(list(partition))
                    
        return result
        
    def is_palin(self, s):
        l = 0
        r = len(s) - 1
        while (l < r):
            if (s[l] != s[r]):
                return False
            l += 1
            r -= 1
        
        return True
