from heapq import heappush, heappop
T = int(input())
for _ in range(T):
    J, N = map(int, input().split())
    arr = []
    ans = 0
    for _ in range(N):
        R, C = map(int, input().split())
        heappush(arr, -(R*C))
    while J > 0:
        J += heappop(arr)
        ans += 1
    print(ans)
