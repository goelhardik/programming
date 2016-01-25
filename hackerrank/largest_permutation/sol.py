def find_largest_lex_perm(nums, k, n):
    ind_arr = [0 for i in range(n + 1)] # array to maintain indices of each number
    for i in range(n):
        ind_arr[nums[i]] = i
        
    for i in range(n):
        if (nums[i] != n - i):  # swap required
            tmp = nums[i]
            i2 = ind_arr[n - i]
            # swap index values in ind_arr
            ind_arr[n - i] = i
            ind_arr[nums[i]] = i2
            # swap num values
            nums[i] = n - i
            nums[i2] = tmp
            
            k -= 1
            if (k == 0):
                break
                
    return nums
            

# driver code
n, k = map(int, input().split())
nums = list(map(int, input().split()))
find_largest_lex_perm(nums, k, n)
print(*nums)
