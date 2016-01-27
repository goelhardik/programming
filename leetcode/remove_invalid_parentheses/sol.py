class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        answer = []
        q1 = []
        q2 = []
        q1.append(s)
        while (q1):
            while (q1):
                s = q1.pop()
                if (self.is_valid(s)):
                    if (s not in answer):
                        answer.append(s)
                    continue    # no need to append its children; max length has been found
                if (len(s) == 1):
                    continue
                for i in range(len(s)):
                    if (s[i] != '(' and s[i] != ')'):   # if not parentheses
                        continue
                    q2.append(s[ : i] + s[i + 1 : ])
                    
            if (answer):
                break
            q1 = q2
            q2 = []
        
        return answer
        
    def is_valid(self, s):
        stack = []
        for c in s:
            if (c != '(' and c != ')'):
                continue
            if (c == '('):
                stack.append(c)
            else:
                if (not stack):
                    return False
                stack.pop()
                
        if (stack):
            return False
        return True

s = "((()((s((((()"
ob = Solution()
print(ob.removeInvalidParentheses(s))
