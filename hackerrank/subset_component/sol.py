def find_set_of_one_bits(num):
    count = 0
    ones = set()
    while (num > 0):
        if (num & 1):
            ones.add(count)
        num >>= 1
        count += 1
    if (len(ones) <= 1):
        return set()
    return ones

"""
nums - array of input numbers
l - desired subset length
count - length of current subset
start - start position for adding next element
n - total number of elements in nums
edges - set of all nodes with edges in the current subset
bits - map constructed earlier containing edge nodes for each number in nums
"""
def get_subsets(nums, l, count, start, n, edges, bits):
    if (n - start < l - count): # subset of length l not possible starting at start
        return 0
    if (count == l):
        length = len(edges)
        if (length <= 1):
            ans = 64
        else:
            ans = 64 - length + 1
        return ans  # number of independent components for this subset of nums
    total = 0
    for i in range(start, n):
        total += get_subsets(nums, l, count + 1, i + 1, n, edges.union(bits[nums[i]]), bits)
    return total

def find_sum_connected_comp(nums, n):
    bits = {}   # to store 1 bits for each number in nums
    for i in range(n):
        bits[nums[i]] = find_set_of_one_bits(nums[i])

    # iterate over all possible sets
    sum = 0
    for l in range(n + 1):  # iterate over all lengths of sets
        edges = set()
        # add number of independent components for all subsets of length l
        sum += get_subsets(nums, l, 0, 0, n, edges, bits)
    
    return sum

# driver code
n = int(input())
nums = list(map(int, input().split()))
print(find_sum_connected_comp(nums, n))
