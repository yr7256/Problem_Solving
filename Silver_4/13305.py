N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
result = 0
c = cost[0]
for i in range(N-1):
    if cost[i] < c:
        c = cost[i]
    result += c*dist[i]
print(result)
