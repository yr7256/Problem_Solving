'''
순서 정하기
위상정렬로 depth 작은 애들부터 넣고 차수 빼기
'''
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
depth = [0]*(N+1)
for i in range(M):
    PD = list(map(int, input().split()))
    length, sequence = PD[0], PD[1:]
    for i in range(length-1):
        graph[sequence[i]].append(sequence[i+1])
        depth[sequence[i+1]] += 1
# print(graph)
# print(depth)
ans = []
queue = deque([])
for i in range(1, N+1):
    if not depth[i]:
        queue.append(i)
# print(queue)
while queue:
    current = queue.popleft()
    ans.append(current)
    for next in graph[current]:
        depth[next] -= 1
        if not depth[next]:
            queue.append(next)
if len(ans) == N:
    for i in ans:
        print(i)
else:
    print(0)
