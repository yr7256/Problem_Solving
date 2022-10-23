N = int(input())
A = list(map(int, input().split()))
S = 0
for i in range(len(A)):
    S += A[i]/max(A)
print((S/len(A))*100)
