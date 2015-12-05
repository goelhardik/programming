class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map = {}
        for i in range(len(nums)):
            if (nums[i] in map):
                if (abs(map[nums[i]] - i) <= k):
                    return True
            
            # update the map anyway; deals with duplicate elements
            map[nums[i]] = i
                
        return False
