from collections import defaultdict
import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]*2
s, e = 0, k-1
dic = defaultdict(int)
for i in range(e+1):
    dic[arr[i]] += 1
dic[c] += 1
ans = 0
while s < N:
    ans = max(len(dic), ans)
    dic[arr[s]] -= 1
    if not dic[arr[s]]:
        del dic[arr[s]]
    s += 1
    e += 1
    dic[arr[e]] += 1
print(ans)
