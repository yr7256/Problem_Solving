N = int(input())
ans = 0
k = 1
while N > 0:
    if N < k:
        k = 1
    N -= k
    k += 1
    ans += 1
print(ans)
