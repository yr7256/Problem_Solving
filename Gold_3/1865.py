import sys
imput = sys.stdin.readline
INF = sys.maxsize


def Bellman_Ford(start):
    distance[start] = 0
    for i in range(N):
        for j in range(1, N+1):
            for arr, cost in route[j]:
                if distance[arr] > distance[j]+cost:
                    distance[arr] = distance[j]+cost
                    if i == N-1:
                        return True
    return False


TC = int(input())
for i in range(TC):
    N, M, W = map(int, input().split())
    route = [[] for i in range(N+1)]
    distance = [INF]*(N+1)
    for j in range(M):
        S, E, T = map(int, input().split())
        route[S].append((E, T))
        route[E].append((S, T))
    for k in range(W):
        S, E, T = map(int, input().split())
        route[S].append((E, -T))
    ans = Bellman_Ford(1)
    if not ans:
        print('NO')
    else:
        print('YES')
