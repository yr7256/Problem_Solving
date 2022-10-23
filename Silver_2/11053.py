N = int(input())
A = list(map(int, input().split()))
B = [1]*N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and B[i] < B[j]+1:
            B[i] = B[j]+1
print(max(B))
