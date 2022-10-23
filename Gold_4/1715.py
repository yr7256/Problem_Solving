import heapq
N = int(input())
card = []
result = 0
for i in range(N):
    heapq.heappush(card, int(input()))
if len(card) == 1:
    print(0)
else:
    while len(card) > 1:
        combine = heapq.heappop(card)+heapq.heappop(card)
        result += combine
        heapq.heappush(card, combine)
    print(result)
