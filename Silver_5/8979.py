import sys
input = sys.stdin.readline
N, K = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]
C.sort(key=lambda x: (-x[1], -x[2], -x[3]))
for i in range(N):
    if C[i][0] == K:
        num = i
for j in range(N):
    if C[num][1:] == C[j][1:]:
        print(j+1)
        break
