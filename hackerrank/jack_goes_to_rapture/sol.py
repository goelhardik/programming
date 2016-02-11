from heapq import *

def create_adj_list(adj, n, edges, e):
    for edge in edges:
        adj[edge[0]][edge[1]] = edge[2]
        adj[edge[1]][edge[0]] = edge[2]

def find_min_fare(n, edges, e):
    MAX = float("inf")
    adj = [{} for i in range(n + 1)]
    create_adj_list(adj, n, edges, e)
    unvisited = set([i for i in range(1, n + 1)])	# set of unvisited nodes
	# use heap for fast minimum access
    heap = []
    heappush(heap, (0, 1))	# push tuples of form (fare, node)
    fare = [MAX for i in range(n + 1)]
    fare[1] = 0
    while (unvisited and heap):
        # find the guy with minimum fare
        min_node = heappop(heap)	# get tuple with minimum fare
        min_fare = min_node[0]
        min_node = min_node[1]
        if (min_fare == MAX):
            break
		# workaround for not being able to modify entries in the heap
        if (min_node not in unvisited):	# since we cannot modify values in heap
            continue	# it is possible that a visited node is there in the heap
        for neighbor in adj[min_node]:
            if (neighbor not in unvisited):
                continue
            alt_fare = max(adj[min_node][neighbor] - fare[min_node], 0)
            alt_fare += fare[min_node]
            if (alt_fare < fare[neighbor]):
                fare[neighbor] = alt_fare
            if (fare[neighbor] == MAX):	# don't add unreachable nodes to heap
                continue	# no need to grow its size
            heappush(heap, (fare[neighbor], neighbor))
			# duplicate nodes might get added, but we will always get the 
			# minimum node while we are doing pop
                
                
        unvisited.remove(min_node)
        
    if (fare[n] == MAX):
        return "NO PATH EXISTS"
    else:
        return fare[n]
            

# driver code
n, e = map(int, input().split())
edges = []
for i in range(e):
    n1, n2, c = map(int, input().split())
    edges.append([n1, n2, c])
print(find_min_fare(n, edges, e))
