class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if (t < 0):
            return False
        t += 1
        buckets = {}
        for i in range(len(nums)):
            if (i > k):
                del buckets[nums[i - k - 1] // t]
                
            bucket = nums[i] // t
            if (bucket in buckets):
                return True
            if (bucket - 1 in buckets and abs(nums[i] - buckets[bucket - 1]) < t):
                return True
            if (bucket + 1 in buckets and abs(nums[i] - buckets[bucket + 1]) < t):
                return True
                
            buckets[bucket] = nums[i]
            
        return False
