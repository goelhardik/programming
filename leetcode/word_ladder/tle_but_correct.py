class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        q1 = []
        q2 = []
        q1.append(beginWord)
        remaining = set(wordList)
        level = 0
        while (q1):
            while (q1):
                visited = set()
                word = q1.pop()
                if (self.is_valid_trans(word, endWord)):
                    return level + 2
                for nextword in remaining:
                    if (self.is_valid_trans(word, nextword)):
                        visited.add(nextword)
                        q2.append(nextword)
                for temp in visited:
                    remaining.remove(temp)
                    
            q1 = q2
            q2 = []
            level += 1
            
        return 0
                        
    def is_valid_trans(self, w1, w2):
        diff_c = 0
        for c, d in zip(w1, w2):
            if (c != d):
                diff_c += 1
                
        if (diff_c == 1):
            return True
        else:
            return False
