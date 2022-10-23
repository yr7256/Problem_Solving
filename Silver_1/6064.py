import sys
from math import lcm
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    ans = -1
    while x <= lcm(M, N):
        if x % N == y % N:
            ans = x
            break
        x += M
    print(ans)
