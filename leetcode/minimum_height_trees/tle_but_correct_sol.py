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
        min_h = float("inf")
        min_root = []
        # taking each node as root, do BFS and update height
        for node in range(n):
            h = 0
            visited = [0 for i in range(n)]
            q1 = []
            q2 = []
            q1.append(node)
            while (len(q1) > 0):
                while (len(q1) > 0):
                    parent = q1.pop(0)
                    visited[parent] = 1
                    for child in adj[parent]:
                        if (visited[child] == 0):
                            q2.append(child)
                q1 = q2
                q2 = []
                h += 1
            # update the minimum possible height if required
            if (h < min_h):
                min_h = h
                min_root = [node]
            elif (h == min_h):
                min_root.append(node)
        
        return min_root
        
    def make_adj_list(self, edges, adj):
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
