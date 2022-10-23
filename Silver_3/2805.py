import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
L = 1
U = max(A)
while L <= U:
    mid = (L+U)//2
    count = 0
    for i in A:
        if i > mid:
            count += i-mid
            if count > M:
                break
    if count >= M:
        L = mid+1
    else:
        U = mid-1
print(U)
