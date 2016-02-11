def find_min_moves(n, ladders, m, snakes):
    q1 = []
    q1.append(1) # starting node
    edges = [i for i in range(1, 7)]    # possible die roles
    q2 = []
    moves = 0
    visited = [0 for i in range(101)]
    visited[1] = 1
    while (q1):
        while (q1):
            node = q1.pop()
            if (node == 100):
                return moves
            
            for edge in edges:
                new_node = node + edge
                if (new_node > 100):
                    break
                if (visited[new_node] == 1):    # already visited; no need to check again
                    continue
                visited[new_node] = 1
                if (new_node in snakes):    # go down
                    new_node = snakes[new_node]
                    q2.append(new_node)
                    continue
                if (new_node in ladders):   # go up
                    new_node = ladders[new_node]
                    q2.append(new_node)
                    continue
                q2.append(new_node)
        q1 = q2
        q2 = []
        moves += 1
                
    return -1

# driver code
t = int(input())
for i in range(t):
    n = int(input())
    ladders = {}
    for j in range(n):
        s, e = map(int, input().split())
        ladders[s] = e
    m = int(input())
    snakes = {}
    for k in range(m):
        s, e = map(int, input().split())
        snakes[s] = e
    
    print(find_min_moves(n, ladders, m, snakes))
