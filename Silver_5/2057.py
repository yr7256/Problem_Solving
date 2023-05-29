from math import factorial

lst = [factorial(i) for i in range(21)]
N = int(input())
if N == 0:
    print('NO')
else:
    for i in range(20, -1, -1):
        if N == 0:
            print('YES')
            exit()
        else:
            if N >= lst[i]:
                N -= lst[i]
    print('NO' if N else 'YES')