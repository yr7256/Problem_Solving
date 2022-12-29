import sys
import heapq
input = sys.stdin.readline
N = int(input())
lst = []
for i in range(N):
    s, e = map(int, input().split())
    lst.append((s, e))
lst.sort()
# print(lst)
rooms = [0]
ans = 1
for s, e in lst:
    if s >= rooms[0]:
        heapq.heappop(rooms)
    else:
        ans += 1
    heapq.heappush(rooms, e)
print(ans)
