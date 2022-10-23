
def P_n(i):
    if i == 1:
        return False
    else:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                return False
        return True


def happy(x):
    a = []
    for i in str(x):
        a.append(i)
    b = 0
    for j in a:
        b += int(j)**2
    if
    happy(b)


A = []
for i in range(2, 10001):
    if P_n(i) == True:
        A.append(i)

P = int(input())
for i in range(P):
    i, N = map(int, input().split())
    if not N in A:
        print(i, N, 'NO')
    else:
        if
