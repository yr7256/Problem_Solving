from math import ceil
N = int(input())
arr = list(map(int, input().split()))
T, P = map(int, input().split())
ans = 0
for i in arr:
    ans += ceil(i/T)
print(ans)
print(N//P, N % P)
