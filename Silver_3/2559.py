N, K = map(int, input().split())
temp = list(map(int, input().split()))
s = sum(temp[:K])
A = [s]
for i in range(N-K):
    s = s-temp[i]+temp[i+K]
    A.append(s)
print(max(A))
