from itertools import combinations
from collections import deque


def dfs(n):  # n 그룹 돌아볼거임
    start = n[0]
    queue = deque([start])
    visited = [start]
    result = 0
    while queue:
        x = queue.pop()
        result += people[x]
        # print(route[x])
        for next in route[x]:
            if next not in visited and next in n:
                queue.append(next)
                visited.append(next)
    return result, len(visited)


N = int(input())
route = [[] for _ in range(N+1)]
people = [0] + list(map(int, input().split()))
ans = 10000
for i in range(N):
    route[i+1] = list(map(int, input().split()))[1:]
for i in range(1, N//2+1):
    combi = set(combinations(range(1, N+1), i))
    for c in combi:
        a = list(set(range(1, N+1)) - set(c))
        A, lenA = dfs(a)
        C, lenC = dfs(c)
        if lenA + lenC == N:
            ans = min(ans, abs(A-C))
if ans == 10000:
    print(-1)
else:
    print(ans)
# print(people)
# print(route)
