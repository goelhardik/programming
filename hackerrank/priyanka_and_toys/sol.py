def find_min_buying_units(weights, n):
    weights.sort()  # sort the weights
    i = 0
    units = 0   # track number of units
    while (i < n):
        w = weights[i]
        units += 1
        i += 1
        # skip the maximum number of toys that can be bought with ith toy's weight
        while (i < n and weights[i] >= w and weights[i] <= w + 4):
            i += 1
            
    return units
        
# driver code
n = int(input())
weights = list(map(int, input().split()))
print(find_min_buying_units(weights, n))
