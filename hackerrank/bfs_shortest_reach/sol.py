def create_adjacency_list(adj, edges):
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])
    
def shortest_reaches(n, edges, start_node):
    adj = [[] for i in range(n + 1)]
    create_adjacency_list(adj, edges)   # create adjacency matrix from edges
    shortest_dist = [-1 for i in range(n + 1)]  # list to maintain shortest distances
    q1 = []
    q2 = []
    q1.append(start_node)
    level = 1   # to track number of edges traversed
    visited = set()     # set to keep visited nodes
    visited.add(start_node)
    # use BFS to find the shortest number of edges required to be traversed
    while (q1):
        while (q1):
            node = q1.pop()
            for child in adj[node]:
                if (child not in visited):
                    visited.add(child)
                    shortest_dist[child] = 6 * level
                    q2.append(child)
                    
        level += 1
        q1 = q2
        q2 = []
    
    del shortest_dist[start_node]
    del shortest_dist[0]
    return shortest_dist

# driver code
tests = int(input())
for i in range(tests):
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        n1, n2 = map(int, input().split())
        edges.append([n1, n2])
    start = int(input())
    dist = shortest_reaches(n, edges, start)
    print(*dist)
