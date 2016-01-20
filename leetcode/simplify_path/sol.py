class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if (len(path) == 0):
            return ""
        stack = []
        path = path.split("/")
        for item in path:
            if (item == "."):
                pass
            elif (item == ".."):
                if (len(stack) == 0):
                    pass
                else:
                    stack.pop()
            elif (item == ""):
                pass
            else:
                stack.append(item)
                
        ans = "/".join(stack)
        ans = "/" + ans
            
        return ans
