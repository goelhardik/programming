n, m = map(int, input().split())
nums = [0 for i in range(n)]
for i in range(m):
    a, b, k = map(int, input().split())
    nums[a - 1] += k
    if (b < n):
        nums[b] -= k
       
max = -float("inf")
sum = 0 # sum represents the value at current index
for i in range(n):
    sum += nums[i]
    if (sum > max):
        max = sum
        
print(max)
