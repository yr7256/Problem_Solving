from collections import defaultdict
g, l = map(int, input().split())
W = input()
S = input()
W_lst = defaultdict(int)
S_lst = defaultdict(int)
start, target, ans = 0, 0, 0
for i in range(g):
    W_lst[W[i]] += 1
for i in range(l):
    S_lst[S[i]] += 1
    target += 1
    if target == g:
        if W_lst == S_lst:
            ans += 1
        S_lst[S[start]] -= 1
        if not S_lst[S[start]]:
            del S_lst[S[start]]
        start += 1
        target -= 1
print(ans)
