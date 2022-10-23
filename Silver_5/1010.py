def fac(n):
    if n <= 1:
        return 1
    return n * fac(n-1)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(fac(M)//(fac(M-N)*fac(N)))
