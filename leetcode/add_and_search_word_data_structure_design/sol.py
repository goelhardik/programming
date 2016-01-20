class Node(object):
    def __init__(self, x = ""):
        self.val = x
        self.children = [None for i in range(26)]
        self.value = 0
        
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        # use a Trie as a data structure
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        p = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if (p.children[ind] == None):
                p.children[ind] = Node(c)
            p = p.children[ind]
        
        p.value = len(word)
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        q = []
        q2 = []
        p = self.root
        q.append(p)
        for c in word:
            if (not q):
                return False
            if (c == "."):  # if it's a dot, add all possible nodes to the queue
                while (q):
                    node = q.pop(0)
                    for child in node.children:
                        if (child != None):
                            q2.append(child)
            else:   # append only possibly correct nodes
                ind = ord(c) - ord('a')
                while (q):
                    node = q.pop(0)
                    if (node.children[ind] == None):
                        continue
                    q2.append(node.children[ind])
            q = q2
            q2 = []
                
        while (q):
            node = q.pop()
            if (node.value != 0):
                return True
        
        return False
        
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
