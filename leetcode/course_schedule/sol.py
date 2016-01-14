class Solution(object):
    def canFinish(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # create an adjacency list from edges
        adj = [[] for i in range(n)]
        self.create_adj_list(edges, adj)
        
        # check for cycles
        rec_stack = []  # recursion stack
        visited = [0 for i in range(n)]     # visited array to keep track of nodes visited in one connected graph
        for node in range(n):
            if (visited[node] == 0):
                if (self.detect_cycle(adj, node, visited, rec_stack)):
                    return False
        
        return True
        
    def create_adj_list(self, edges, adj):
        for edge in edges:
            adj[edge[0]].append(edge[1])
            
    # use DFS to detect cycle; keep track of the recursion stack, if a node reappears, there is a cycle
    def detect_cycle(self, adj, node, visited, rec_stack):
        visited[node] = 1
        if (node in rec_stack):
            return True
        rec_stack.append(node)
        for child in adj[node]:
            if (self.detect_cycle(adj, child, visited, rec_stack)):
                return True
                
        rec_stack.pop()
        return False
