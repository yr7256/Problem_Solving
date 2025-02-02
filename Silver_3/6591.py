import sys
input = sys.stdin.readline
while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    k = min(k, n-k)
    ans = 1
    temp = 1
    for i in range(1, k+1):
        ans *= n
        n -= 1
        temp *= i
    print(ans//temp)
