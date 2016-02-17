def min_dist_helper(m, n, queries, start, r1, r2, map):
    if (n == 0):
        return 0
    if ((start, r1, r2) in map):
        return map[(start, r1, r2)]
    query = queries[start]
    dist = abs(query[1] - query[0])
    if (r1 < 0):
        r1_dist = min_dist_helper(m, n - 1, queries, start + 1, query[1], r2, map)
    else:
        r1_dist = min_dist_helper(m, n - 1, queries, start + 1, query[1], r2, map) + abs(query[0] - r1)
    if (r2 < 0):
        r2_dist = min_dist_helper(m, n - 1, queries, start + 1, r1, query[1], map)
    else:
        r2_dist = min_dist_helper(m, n - 1, queries, start + 1, r1, query[1], map) + abs(query[0] - r2)
    
    map[(start, r1, r2)] = min(r1_dist, r2_dist) + dist
    return map[(start, r1, r2)]

def find_min_dist(m, n, queries):
    return min_dist_helper(m, n, queries, 0, -1, -1, {})
        
# driver code
t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    queries = []
    for j in range(n):
        a, b = map(int, input().split())
        queries.append([a, b])
    print(find_min_dist(m, n, queries))
