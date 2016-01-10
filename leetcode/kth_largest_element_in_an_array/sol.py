class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while (low <= high):
            # select mid and partition the array around it
            mid = (low + high) // 2
            q = self.partition(nums, low, high, mid)
            if (high - q + 1 == k):
                return nums[q]
            # select the appropriate half of the array
            elif (high - q + 1 > k):
                low = q + 1
            else:
                k = k - (high - q + 1)
                high = q - 1
                
    # partition the array around the index q
    def partition(self, nums, low, high, q):
        if (low >= high):
            return low
        self.swap(nums, high, q)
        l = low - 1
        i = low
        while (i < high):
            if (nums[i] < nums[high]):
                l += 1
                self.swap(nums, i, l)
            i += 1
        l += 1
        self.swap(nums, l, high)
        return l
        
    def swap(self, nums, x, y):
        tmp = nums[x]
        nums[x] = nums[y]
        nums[y] = tmp
