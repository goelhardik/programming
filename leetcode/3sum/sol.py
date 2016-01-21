class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            # avoid duplicates
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            target = -nums[i]
            l = i + 1
            r = n - 1
            while (l < r):
                sum = nums[l] + nums[r]
                if (sum == target):
                    alist = [nums[i], nums[l], nums[r]]
                    ans.append(alist)
                    l += 1
                    r -= 1
                    # avoid duplicates
                    while (l < r and nums[l] == nums[l - 1]):
                        l += 1
                    while (l < r and nums[r] == nums[r + 1]):
                        r -= 1
                elif (sum < target):
                    l += 1
                else:
                    r -= 1
                    
        return ans
