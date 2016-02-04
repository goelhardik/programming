def find_closest_sum(nums, n, k):
    dp = [0 for i in range(k + 1)]
    dp[0] = 1
    max_ind = 0
    for num in nums:
        i = 0
        while (1):
            ind = i + num
            if (ind > k):
                break
            if (dp[i] == 1):
                dp[ind] = 1
                if (ind == k):
                    return k
                max_ind = max(ind, max_ind)
            i += 1
            
    return max_ind
    

# driver code
tests = int(input())
for i in range(tests):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(find_closest_sum(nums, n, k))
