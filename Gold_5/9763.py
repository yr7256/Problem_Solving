# 3중 for문 사용하면 시간초과 (마을의 수가 최대 10000)
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 1e9
for i in range(N):
    d1, d2 = 1e9, 1e9
    x1, y1, z1 = arr[i]
    for j in range(N):
        if i == j:
            continue
        x2, y2, z2 = arr[j]
        temp = abs(x1-x2)+abs(y1-y2)+abs(z1-z2)
        if d1 > temp:
            d2 = d1
            d1 = temp
        else:
            d2 = min(d2, temp)
    ans = min(d1+d2, ans)
print(ans)
