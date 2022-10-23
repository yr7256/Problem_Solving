N, K = map(int, input().split())
weight = [0]
value = [0]
for _ in range(N):
    W, V = map(int, input().split())
    weight.append(W)
    value.append(V)
bag = [[0 for i in range(K+1)] for i in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        if weight[i] <= j:
            bag[i][j] = max(bag[i-1][j], value[i]+bag[i-1][j-weight[i]])
        else:
            bag[i][j] = bag[i-1][j]
print(bag[N][K])
