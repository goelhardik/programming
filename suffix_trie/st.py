class SuffixTrie():

    def __init__(self, t):
        t += '$'    # special symbol to denote leaf nodes; helps to identify 
                    # suffixes
        self.root = {}
        for i in range(len(t)):
            cur = self.root
            for c in t[i : ]:
                if (c not in cur):
                    cur[c] = {}
                cur = cur[c]

    def follow_path(self, s):
        cur = self.root
        for c in s:
            if (c not in cur):
                return None
            cur = cur[c]
        return cur

    def is_substr(self, s):
        node = self.follow_path(s)
        if (node == None):
            return False
        return True

    def is_suffix(self, s):
        node = self.follow_path(s)
        if (node == None or '$' not in node):
            return False
        return True

    def count_leaves(self, node):
        if (not node):
            return 1
        count = 0
        for c in node:
            count += self.count_leaves(node[c])

        return count

    def num_occur(self, s):
        node = self.follow_path(s)
        if (node == None):
            return 0 
        leaves = self.count_leaves(node)
        return leaves

st = SuffixTrie('banana')
print(st.is_substr('ban'))
print(st.is_substr('bab'))
print(st.is_substr('ana'))
print(st.is_suffix('banana'))
print(st.is_suffix('nana'))
print(st.is_suffix('ban'))
print(st.num_occur('ana'))
print(st.num_occur('banana'))
print(st.num_occur('bnana'))
print(st.num_occur('a'))
