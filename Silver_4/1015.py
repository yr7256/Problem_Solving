N = int(input())
A = list(map(int, input().split()))
arr = [-1]*N
for i in range(N):
    num = A.index(min(A))
    arr[num] = i
    A[num] = 1001
print(*arr)
