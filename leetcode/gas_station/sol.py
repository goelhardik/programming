class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        """
        If the total of gas and cost difference is non negative, it means that 
        the circuit can be completed.
        Also if at any point the total gas in the tank is negative, it means 
        that the start point cannot be before that point. So we can safely 
        ignore the start points upto that point.
        """
        tank = 0
        start = 0
        total = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            if (tank >= 0):
                tank += diff
            else:
                tank = diff
                start = i
            
            total += diff
            
        if (total >= 0):
            return start
        else:
            return -1
