class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # find the xor of all the numbers
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
            
        # find the lsb of the ans, which is set
        bit = 0
        while (ans % 2 == 0):
            ans >>= 1
            bit += 1
        
        # partition the list into two - one with the bit set, one with the bit cleared
        # the single numbers will be in separate lists
        # all other numbers in each list will have copies of themselves in the same list
        # xor the two lists to give the two single numbers
        mask = 1 << bit
        ans1 = 0
        ans2 = 0
        for i in range(len(nums)):
            if (nums[i] & mask):
                ans1 ^= nums[i]
            else:
                ans2 ^= nums[i]
                
        return [ans1, ans2]
