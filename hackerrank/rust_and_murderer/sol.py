def find_shortest_dist(adj, n, m, start):
    unvisited = set([i for i in range(1, n + 1)]) # set not touched yet
    q = set([start]) # set being currently explored
    unvisited.remove(start)
    dist = [0 for i in range(n + 1)]
    while (unvisited):
        # pick up a node from exploring set
        min_node = q.pop()
        min_dist = dist[min_node]
         
        new_dist = min_dist + 1
        del_list = []
        for node in unvisited:
            # only add the nodes that do not have edges from here
            if (node in adj[min_node]):
                continue
            del_list.append(node)
            # otherwise update distance to this neighbor
            dist[node] = new_dist
            
        for node in del_list:
            q.add(node)    # add to exploring set
            unvisited.remove(node)  # remove from untouched set
            
        
    del dist[start]
    del dist[0]
    return dist
        

# driver code
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    adj = [set() for k in range(n + 1)]
    for j in range(m):
        s, e = map(int, input().split())
        adj[s].add(e)
        adj[e].add(s)
    start = int(input())
    ans = find_shortest_dist(adj, n, m, start)
    print(*ans)
