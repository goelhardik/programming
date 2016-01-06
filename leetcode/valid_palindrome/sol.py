class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # convert string to lower case
        s = s.lower()
        # set ascii limits for comparable characters
        clower = ord('a')
        cupper = ord('z')
        nlower = ord('0')
        nupper = ord('9')
        i = 0
        j = len(s) - 1
        while (i < j):
            left = ord(s[i])
            right = ord(s[j])
            # compare the two indices if valid characters
            if ((left > cupper or left < clower) and (left > nupper or left < nlower)):
                i += 1
            elif ((right > cupper or right < clower) and (right > nupper or right < nlower)):
                j -= 1
            else:
                if (left != right):
                    return False
                else:
                    i += 1
                    j -= 1
                    
        return True
