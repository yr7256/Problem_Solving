import sys
input = sys.stdin.readline
N = int(input())
x0, x1, y0, y1 = 10000, -10000, 10000, -10000
for i in range(N):
    a, b = map(int, input().split())
    x0 = min(x0, a)
    x1 = max(x1, a)
    y0 = min(y0, b)
    y1 = max(y1, b)
if N > 1:
    print((x1-x0)*(y1-y0))
else:
    print(0)
