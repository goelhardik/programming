def find_min_abs_sum(n, k, nums):
    # minimum unfairness can only be obtained using contiguous elements in sorted array
    nums.sort()
    unfair = 0
    runsum = nums[0]
    # find unfairness for first k elements
    for i in range(1, k):
        unfair += i * nums[i] - runsum
        runsum += nums[i]
    minun = unfair
    # update unfairness for all remaining combinations in O(1)
    for i in range(k, n):
        runsum -= nums[i - k]
        unfair += (k - 1) * (nums[i] + nums[i - k]) - 2 * runsum
        minun = min(minun, unfair)
        runsum += nums[i]
        
    return minun

# driver code
n = int(input())
k = int(input())
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)
print(find_min_abs_sum(n, k, nums))
