class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s = list(s) # convert immutable string to list
        self.reverse_list(s, 0, n - 1)  # reverse the entire string first
        l = 0
        ans = ""
        while (1):
            while (l < n and s[l] == " "):  # skip all whitespaces to find the left end of a word
                l += 1
            if (l >= n):
                break
            r = l + 1
            while (r < n and s[r] != " "):  # find the right end of the word (until list end or space is encountered)
                r += 1
            self.reverse_list(s, l, r - 1)  # reverse the individual word
            ans += "".join(s[l : r]) + " "  # add the reversed word and a space to ans
            l = r   # update left end to right end
            
        if (ans and ans[-1] == " "):
            ans = ans[0 : len(ans) - 1]
        return ans
        
    def reverse_list(self, s, l, r):
        while (l < r):
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
