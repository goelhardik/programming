class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        """
        Starting from each station, move forward and check if we ever run out
        of gas
        """
        for i in range(len(gas)):
            totalgas = 0
            for j in range(len(gas)):
                totalgas += gas[(i + j) % len(gas)] - cost[(i + j) % len(gas)]
                if (totalgas < 0):
                    break
            if (totalgas >= 0):
                return i
                
        return -1
