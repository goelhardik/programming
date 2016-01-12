class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            # only if there is a zero, it is possible that the next number is not reachable
            if (nums[i] == 0):
                flag = 1
                if (i == n - 1):
                    return True
                for k in range(i, -1, -1):
                    # check if the next number is reachable
                    if (nums[k] + k >= i + 1):
                        flag = 0
                        break
                # if next number is not reachable, we can't go any further
                if (flag == 1):
                    return False
                    
        return True
