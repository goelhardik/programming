class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for i in range(len(strs)):
            copy = strs[i]
            copy = ''.join(sorted(copy))
            if (copy in map):
                map[copy].append(strs[i])
            else:
                map[copy] = [strs[i]]
                
        result = []
        for alist in map.values():
            alist.sort()
            result.append(alist)
            
        return result
