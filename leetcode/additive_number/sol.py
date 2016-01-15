class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        """
        Consider every possible choice of the first two numbers.
        Start parsing the remaining string according to their sum.
        If the string becomes empty, then we have a solution!
        """
        for l1 in range(1, n):
            n1 = int(num[ : l1])
            # check for number starting from 0
            if (n1 > 0 and num[0] == '0'):
                continue
            
            for l2 in range(1, n - l1):
                n2 = int(num[l1 : l1 + l2])
                # check for number starting from 0
                if (n2 > 0 and num[l1] == '0'):
                    continue
                
                result = []
                # check the remaining string now
                if (self.check_rem(num[l1 + l2 : ], n1, n2, result)):
                    if (len(result) > 0):
                        return True
                        
        return False
        
    def check_rem(self, num, n1, n2, result):
        if (len(num) == 0):
            return True
            
        sum_n = n1 + n2
        # check for number starting from 0
        if (sum_n > 0 and num[0] == '0'):
            return False
            
        sum_n_str = str(sum_n)
        l = len(sum_n_str)
        if (l > len(num)):
            return False
        if (num[ : l] == sum_n_str):
            result.append(sum_n)
            n1 = n2
            n2 = sum_n
            return self.check_rem(num[l : ], n1, n2, result)
        
        return False
