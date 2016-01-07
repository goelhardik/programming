class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        self.generate_paren(n, n, "", out)
        return out
    
    # o and c represent the number of remaining open and closing parentheses
    def generate_paren(self, o, c, item, out):
        if (o > c):
            return
        if (o == 0 and c == 0):
            out.append(item)
            return
        
        if (o > 0):
            self.generate_paren(o - 1, c, item + "(", out)
        if (c > 0):
            self.generate_paren(o, c - 1, item + ")", out)
