import heapq
K, N = map(int, input().split())
prime = list(map(int, input().split()))
queue = prime[:]
heapq.heapify(queue)
for _ in range(N):
    num = heapq.heappop(queue)
    for p in prime:
        heapq.heappush(queue, num*p)
        if num % p == 0:
            break
print(num)
