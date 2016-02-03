def create_adjacency_list(adj, edges):
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

def dfs(adj, n, removable, parent, visited):
    count = 1
    visited.add(parent)
    for child in adj[parent]:
        if (child in visited):
            continue
        child_count = dfs(adj, n, removable, child, visited)
        if (child_count % 2 == 0):  # if child count is even, this child can be dislodged
            removable.append([parent, child])
        count += child_count
    return count

def find_removable_edges(n, m, edges):
    adj = [[] for i in range(n + 1)]
    create_adjacency_list(adj, edges)
    removable = []
    dfs(adj, n, removable, 1, set())
    return (len(removable))

# driver code
n, m = map(int, input().split())
edges = []
for i in range(m):
    x, y = map(int, input().split())
    edges.append([x, y])
print(find_removable_edges(n, m, edges))
