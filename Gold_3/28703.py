from heapq import heappop, heappush, heapify
N = int(input())
arr = list(map(int, input().split()))
heapify(arr)
min_num, max_num = min(arr), max(arr)
curr = max_num
ans = max_num-min_num
while arr[0] < max_num:
    temp = heappop(arr)
    ans = min(ans, curr-temp)
    heappush(arr, 2*temp)
    curr = max(curr, 2*temp)
ans = min(ans, curr-arr[0])
print(ans)
