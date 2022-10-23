import sys
from itertools import combinations
N = int(input())
lst = []
ans = sys.maxsize
lst = [list(map(int, input().split())) for _ in range(N)]
combi = [list(combinations(lst, i)) for i in range(1, N+1)]
for com in combi:
    for c in com:
        sour = 1
        bitter = 0
        for i in c:
            sour *= i[0]
            bitter += i[1]
        ans = min(ans, abs(sour-bitter))
print(ans)
