class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for i in range(numCourses)]
        self.create_adj_list(prerequisites, adj)
        visited = [0 for i in range(numCourses)]
        ans = []
        for node in range(numCourses):
            if (visited[node] == 0):
                rec_set = set()
                # if cycle, return empty list
                if (self.dfs(adj, node, ans, rec_set, visited) < 0):
                    return []
                    
        return ans
        
    # do topological sort via DFS and store in ans; return -1 if cycle
    def dfs(self, adj, node, ans, rec_set, visited):
        visited[node] = 1
        rec_set.add(node)
        for neighbor in adj[node]:
            if (neighbor in rec_set):
                return -1
            if (visited[neighbor] == 0):
                if (self.dfs(adj, neighbor, ans, rec_set, visited) < 0):
                    return -1
                
        ans.append(node)
        rec_set.remove(node)
        return 0
        
    def create_adj_list(self, edges, adj):
        for edge in edges:
            adj[edge[0]].append(edge[1])
