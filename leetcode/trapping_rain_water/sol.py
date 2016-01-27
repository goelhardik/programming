class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if (n == 0):
            return 0
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]
        
        # forward pass; update maximum possible height that can be stored
        left[0] = height[0]
        max = left[0]
        for i in range(1, n):
            if (height[i] > max):
                max = height[i]
            left[i] = max
         
        # backward pass; update max possible height       
        right[n - 1] = height[n - 1]
        max = right[n - 1]
        for i in range(n - 2, -1, -1):
            if (height[i] > max):
                max = height[i]
            right[i] = max
        
        # max possible height that can be stored minus the actual height    
        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - height[i]
            
        return water
