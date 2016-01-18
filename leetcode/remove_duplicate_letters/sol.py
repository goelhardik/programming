class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        map = {}
        for i in range(n):
            if (s[i] in map):
                map[s[i]] += 1
            else:
                map[s[i]] = 1
           
        # help from original author http://bookshadow.com/weblog/2015/12/09/leetcode-remove-duplicate-letters/     
        stack = []
        stack_set = set()
        for c in s:
            map[c] -= 1
            if c in stack_set:
                continue
            while (len(stack) > 0 and stack[-1] > c and map[stack[-1]] > 0):
                x = stack.pop()
                stack_set.remove(x)
            stack.append(c)
            stack_set.add(c)
            
        return "".join(stack)
