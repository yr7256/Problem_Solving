import sys
input = sys.stdin.readline
N = int(input())
ex = [int(input()) for i in range(N)]
ex.sort()
ans = 0
for i in range(N):
    ans += abs(i+1-ex[i])
print(ans)
