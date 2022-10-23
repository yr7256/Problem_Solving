import heapq
N = int(input())
heap = []
for i in range(N):
    lst = list(map(int, input().split()))
    if not heap:
        for num in lst:
            heapq.heappush(heap, num)
    else:
        for num in lst:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)
print(heap[0])
