class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
        result = []
        self.letter_comb(digits, 0, "", result, map)
        return result
        
    def letter_comb(self, digits, start, item, result, map):
        if (start == len(digits)):
            if (len(item) > 0):
                result.append(item)
            return
        
        letters = map[digits[start]]
        for i in range(len(letters)):
            item += letters[i]
            self.letter_comb(digits, start + 1, item, result, map)
            item = item[0 : len(item) - 1]
