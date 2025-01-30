from collections import defaultdict
N = int(input())
arr = list(map(int, input().split()))
dic = defaultdict(int)
s, e = 0, 0
ans = 0
while e < N:
    dic[arr[e]] += 1
    while len(dic) > 2:
        dic[arr[s]] -= 1
        if not dic[arr[s]]:
            del dic[arr[s]]
        s += 1
    ans = max(ans, e-s+1)
    e += 1
print(ans)
