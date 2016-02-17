# driver code
a, b, c, d, e, f = map(int, input().split())
w1 = a + b + c + d
w2 = a + b + f
w3 = a + e + d
min_w = min(w1, w2, w3)
if (min_w >= 0):
    print(0)
else:
    print(-min_w)
