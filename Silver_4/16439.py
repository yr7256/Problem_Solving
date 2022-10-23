'''
itertools는 신이다
3개 주문한다고 했으니 combinations로 3개 뽑아서 가장 큰 것 갱신해주자
'''
from itertools import combinations
N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
combi = list(combinations(range(M), 3))
ans = 0
for a, b, c in combi:
    temp = 0
    for i in range(N):
        temp += max(lst[i][a], lst[i][b], lst[i][c])
    ans = max(ans, temp)
print(ans)
