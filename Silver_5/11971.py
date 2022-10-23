import sys
input = sys.stdin.readline
N, M = map(int, input().split())
N_list = []
M_list = []
over = []
for _ in range(N):
    d, s = map(int, input().split())
    N_list += [s]*d
for _ in range(M):
    d, s = map(int, input().split())
    M_list += [s]*d
for i in range(100):
    over.append(M_list[i]-N_list[i])
if max(over) > 0:
    print(max(over))
else:
    print(0)
