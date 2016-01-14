class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        n1 = None
        n2 = None
        c1 = 0
        c2 = 0
        for num in nums:
            if (n1 != None and n1 == num):
                c1 += 1
            elif (n2 != None and n2 == num):
                c2 += 1
            elif (c1 == 0):
                c1 = 1
                n1 = num
            elif (c2 == 0):
                c2 = 1
                n2 = num
            else:
                c1 -= 1
                c2 -= 1
                
        c1 = 0
        c2 = 0
        for num in nums:
            if (num == n1):
                c1 += 1
            elif (num == n2):
                c2 += 1
        
        ans = []
        if (n // 3 < c1):
            ans.append(n1)
        if (n // 3 < c2):
            ans.append(n2)
            
        return ans
