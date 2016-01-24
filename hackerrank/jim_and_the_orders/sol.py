# driver code
n = int(input())
fans = []
for i in range(n):
    ti, di = map(int, input().split())
    fans.append(ti + di)    # append the final delivery time to the list
ans = [(i[0] + 1) for i in sorted(enumerate(fans), key = lambda x:x[1])]    # sort the list based on final delivery time; extract the fan index in sorted order
print(*ans)
