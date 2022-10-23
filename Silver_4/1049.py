import sys
input = sys.stdin.readline
N, M = map(int, input().split())
min_p = 1000
min_pi = 1000
for i in range(M):
    package, piece = map(int, input().split())
    min_p = min(min_p, package)
    min_pi = min(min_pi, piece)
print(min(min_p*((N//6)+1), min_p*(N//6)+min_pi*(N % 6), min_pi*N))
