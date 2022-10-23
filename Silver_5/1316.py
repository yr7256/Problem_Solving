N = int(input())
count = N
for _ in range(N):
    A = input()
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            continue
        elif A[i] in A[i+1:]:
            count -= 1
            break
print(count)
