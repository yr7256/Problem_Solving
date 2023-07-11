import sys
input = sys.stdin.readline
N = int(input())
ans = 1001
for _ in range(N):
    A, B = map(int, input().split())
    if A > B:
        continue
    ans = min(ans, B)
print(ans if ans != 1001 else -1)
