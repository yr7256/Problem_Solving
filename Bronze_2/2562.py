N = []
for _ in range(9):
    A = int(input())
    N.append(A)
print(max(N))
print(N.index(max(N))+1)
