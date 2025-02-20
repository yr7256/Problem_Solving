def solve(k, x):
    if k == 1:
        for i in range(1, 79):
            if A[i] == x:
                return 'YES'
    elif k == 2:
        for i in range(1, 79):
            for j in range(1, 79):
                if A[i]+A[j] == x:
                    return 'YES'
    else:
        for i in range(1, 79):
            for j in range(1, 79):
                for k in range(1, 79):
                    if A[i]+A[j]+A[k] == x:
                        return 'YES'
    return 'NO'


T = int(input())
A = [0, 1, 1]
for i in range(3, 79):
    A.append(A[i-1]+A[i-2])
for _ in range(T):
    k, x = map(int, input().split())
    print(solve(k, x))
