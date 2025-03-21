from heapq import heappop, heappush, heapify
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    heapify(arr)
    ans = 0
    while len(arr) > 1:
        combine = heappop(arr)+heappop(arr)
        ans += combine
        heappush(arr, combine)
    print(ans)
