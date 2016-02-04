def create_adj_list(adj, edges, n):
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

def combinations(edges, n):
    adj = [[] for i in range(n)]
    create_adj_list(adj, edges, n)
    visited = [0 for i in range(n)]
    groups = []
    # identify connected chunks using BFS kind approach
    for i in range(n):
        if (visited[i] == 1):
            continue
        q = []
        q.append(i)
        visited[i] = 1
        count = 0
        while (q):
            node = q.pop()
            count += 1
            for neighbor in adj[node]:
                if (visited[neighbor] == 0):
                    visited[neighbor] = 1
                    q.append(neighbor)
        groups.append(count)
    
    # find total ways to pick a pair
    total_ways = n * (n - 1) // 2
    for x in groups:
        total_ways -= x * (x - 1) // 2
    return total_ways

# driver code
n, l = map(int, input().split())
edges = []
for i in range(l):
    x, y = map(int, input().split())
    edges.append([x, y])
print(combinations(edges, n))
