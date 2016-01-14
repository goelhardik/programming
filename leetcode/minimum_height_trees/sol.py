class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for i in range(n)]
        # make an adjacency list from the edges
        self.make_adj_list(edges, adj)
        if (n == 1):
            return [0]
        if (n == 2):
            return [0, 1]
            
        ans = []
        rem = n
        while (rem > 2):
            del_list = []
            # in each iteration of while loop, remove all nodes of degree 1
            for node in range(n):
                if (adj[node] != None and len(adj[node]) == 1):
                    del_list.append(node)
            for node in del_list:
                adj[adj[node][0]].remove(node)
                adj[node] = None
                rem -= 1
            # when two or fewer nodes remain, they will be the answer
            if (rem <= 2):
                for node in range(n):
                    if (adj[node] != None):
                        ans.append(node)
                return ans
        
    def make_adj_list(self, edges, adj):
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
