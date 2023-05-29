import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    ans = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            if not (i**2+j**2+m) % (i*j):
                ans += 1
    print(ans)
