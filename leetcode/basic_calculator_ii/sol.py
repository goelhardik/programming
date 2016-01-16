class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        op = {"+" : 1, "-" : 1, "*" : 2, "/" : 2}
        num_s = []
        op_s = []
        n = len(s)
        i = 0
        while (i < n):
            if (s[i] == " "):
                i += 1
                continue
            # extract the operator
            elif (s[i] in op):
                op_s.append(s[i])
            # extract the character until next non-digit; save it as a number
            else:
                j = i
                while (j < n and ord(s[j]) <= ord("9") and ord(s[j]) >= ord("0")):
                    j += 1
                num_s.append(int(s[i : j]))
                i = j - 1
                
            # keep solving until it can be solved; but first look if there is a higher precedence operator coming next;
            # if yes, then don't solve yet
            while (len(op_s) > 0 and len(num_s) > len(op_s)):
                # get next operand
                j = i + 1
                while (j < n and s[j] == " "):
                    j += 1
                if (j < n and op[s[j]] > op[op_s[len(op_s) - 1]]):
                    break
                else:
                    n2 = num_s.pop()
                    n1 = num_s.pop()
                    oper = op_s.pop()
                    res = self.operate(n1, n2, oper)
                    num_s.append(res)
            i += 1
            
        if (len(num_s) == 0):
            return 0
        return num_s.pop()
        
    def operate(self, n1, n2, oper):
        if (oper == "+"):
            return n1 + n2
        elif (oper == "-"):
            return n1 - n2
        elif (oper == "*"):
            return n1 * n2
        else:
            return n1 // n2
