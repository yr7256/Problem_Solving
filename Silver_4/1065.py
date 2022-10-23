def h(N):
    s = 0
    for i in range(1, N+1):
        A = list(map(int, str(i)))
        if i < 100:
            s += 1
        elif A[0]-A[1] == A[1]-A[2]:
            s += 1
        elif i == 1000:
            continue
    return s


N = int(input())
print(h(N))
