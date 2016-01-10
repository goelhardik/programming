operators = ["*", "-", "+"]
    
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        result = self.compute_results(0, len(input) - 1, input)
        return result
        
    def no_operator(self, input):
        for i in range(len(input)):
            if (input[i] in operators):
                return False
        return True
        
    def compute_results(self, low, high, input):
        if (self.no_operator(input[low:high + 1])):
            return [int(input[low:high + 1])]
            
        out = []
        for i in range(low, high + 1):
            # for each operator, get results of left side and right side
            if (input[i] in operators):
                left_res = self.compute_results(low, i - 1, input)
                right_res = self.compute_results(i + 1, high, input)
                # combine the results of left and right side in all possible combinations
                for (x, y) in itertools.product(left_res, right_res):
                    out.append(self.operate(x, y, input[i]))
                    
        return list(out)
        
    def operate(self, x, y, operator):
        if (operator == "*"):
            return x * y
        elif (operator == "-"):
            return x - y
        else:
            return x + y
