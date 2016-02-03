def create_adj_list(adj, edges, n):
    for edge in edges:
        if (edge[1] in adj[edge[0]]):
            if (edge[2] >= adj[edge[0]][edge[1]]):
                continue
        adj[edge[0]][edge[1]] = edge[2]
        adj[edge[1]][edge[0]] = edge[2]

MAX = float("inf")

def find_closest_node(mst_set, keys, n):
    min_key = MAX
    for i in range(1, n + 1):
        if (mst_set[i] == 0 and keys[i] < min_key):
            min_key = keys[i]
            min_node = i
            
    return min_node

def prims(n, m, edges, start):
    adj = [{} for i in range(n + 1)]
    create_adj_list(adj, edges, n)
    mst_set = [0 for i in range(n + 1)]
    keys = [MAX for i in range(n + 1)]
    keys[start] = 0
    edge_sum = 0
    for i in range(1, n + 1):
        min_node = find_closest_node(mst_set, keys, n)  # find closest node not in mst_set yet
        mst_set[min_node] = 1
        edge_sum += keys[min_node]
        # update keys of neighbor nodes not in mst_set yet
        for neighbor in adj[min_node]:
            if (mst_set[neighbor] == 0 and adj[min_node][neighbor] < keys[neighbor]):
                keys[neighbor] = adj[min_node][neighbor]
        
    return edge_sum
    

# driver code
n, m = map(int, input().split())
edges = []
for i in range(m):
    x, y, r = map(int, input().split())
    edges.append([x, y, r])
start = int(input())
print(prims(n, m, edges, start))
