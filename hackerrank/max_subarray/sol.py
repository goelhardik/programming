def find_max_subarray_cont(array):
    maxhere = -float("inf")
    maxsub = maxhere
    for i in range(len(array)):
        maxhere = max(maxhere + array[i], array[i])
        maxsub = max(maxhere, maxsub)
        
    return maxsub

def find_max_subarray_non_cont(array):
    max_ele = -float("inf") # track max array element for all negative array
    sum = 0
    zero = 0    # mark presence of zero in the array
    for i in range(len(array)):
        if (array[i] > max_ele):
            max_ele = array[i]
        if (array[i] > 0):
            sum += array[i] # just sum all positive numbers
        elif (array[i] == 0):
            zero = 1
            
    if (sum == 0 and zero == 0):    # all negative array, so sum will be 0
        return max_ele
    else:
        return sum

# driver code
tests = int(input())
for i in range(tests):
    n = int(input())
    array = list(map(int, input().split()))
    
    max_cont = find_max_subarray_cont(array)
    max_non_cont = find_max_subarray_non_cont(array)
    print(max_cont, max_non_cont)
