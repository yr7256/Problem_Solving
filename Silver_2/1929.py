def P_n(i):
    if i == 1:
        return False
    else:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                return False
        return True


M, N = map(int, input().split())
for i in range(M, N+1):
    if P_n(i) == True:
        print(i)
