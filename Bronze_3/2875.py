N, M, K = map(int, input().split())
count = 0
while N+M >= K+3 and N >= 2 and M >= 1:
    N -= 2
    M -= 1
    count += 1
print(count)
