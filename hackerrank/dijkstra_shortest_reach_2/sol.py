def create_adj_list(edges, adj, n):
    for edge in edges:
        if (edge[1] in adj[edge[0]]):   # duplicate edge
            if (edge[2] >= adj[edge[0]][edge[1]]):  # update only if distance is lesser
                continue
        adj[edge[0]][edge[1]] = edge[2]
        adj[edge[1]][edge[0]] = edge[2]
        
def find_shortest_dist(edges, n, start):
    MAX = float("inf")
    adj = [{} for i in range(n + 1)]    # use list of maps to represent graph
    create_adj_list(edges, adj, n)  # create adjacency list
    unvisited = set([i for i in range(1, n + 1)])   # to track unvisited nodes
    dist = [MAX for i in range(n + 1)]  # to track shortest distances
    dist[start] = 0 # start node distance is 0
    while (unvisited):
        min_dist = MAX
        # find the node with the minimum distance value in unvisited set
        for node in unvisited:
            if (dist[node] < min_dist):
                min_dist = dist[node]
                min_node = node
        if (min_dist == MAX):   # only disconnected vertices remaining; so break
            break
        for child in adj[min_node]:
            if (child not in unvisited):
                continue
            alt_dist = dist[min_node] + adj[min_node][child]    # alternate distance for an unvisited node
            if (alt_dist < dist[child]):    # update if required
                dist[child] = alt_dist
                
        unvisited.remove(min_node)  # current node totally examined; remove it
                
    del dist[start]
    del dist[0]
    for i in range(len(dist)):
        if (dist[i] == MAX):
            dist[i] = -1
            
    return dist
                
        

# driver code
tests = int(input())
for i in range(tests):
    n, m = map(int, input().split())
    edges = []
    for j in range(m):
        n1, n2, d = map(int, input().split())
        edges.append([n1, n2, d])
    start = int(input())
    dist = find_shortest_dist(edges, n, start)
    print(*dist)
