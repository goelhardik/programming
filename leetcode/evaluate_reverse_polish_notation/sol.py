class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = set(["+", "-", "*", "/"])
        nums = []
        ops = []
        n = len(tokens)
        for i in range(n):
            if (tokens[i] in operations):
                n2 = nums.pop()
                n1 = nums.pop()
                res = self.operate(n1, n2, tokens[i])
                nums.append(res)
            else:
                nums.append(int(tokens[i]))
                
        return nums.pop()
        
    def operate(self, n1, n2, op):
        if (op == "+"):
            return n1 + n2
        elif (op == "-"):
            return n1 - n2
        elif (op == "*"):
            return n1 * n2
        elif (op == "/"):
            return int(n1 * 1.0 / n2)
