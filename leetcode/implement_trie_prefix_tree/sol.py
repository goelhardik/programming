ALPHABETS = 26

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = 0
        self.children = [None for i in range(ALPHABETS)]

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
    
    def char_to_ind(self, c):
        return (ord(c) - ord('a'))
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        l = len(word)
        for i in range(l):
            ind = self.char_to_ind(word[i])
            # if char is not there already
            if (p.children[ind] == None):
                p.children[ind] = TrieNode()
                
            p = p.children[ind]
            
        p.value = l
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        l = len(word)
        for i in range(l):
            ind = self.char_to_ind(word[i])
            if (p.children[ind] == None):
                return False
            p = p.children[ind]
            
        return (p.value != 0)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        l = len(prefix)
        for i in range(l):
            ind = self.char_to_ind(prefix[i])
            if (p.children[ind] == None):
                return False
            p = p.children[ind]
            
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("somestring")
