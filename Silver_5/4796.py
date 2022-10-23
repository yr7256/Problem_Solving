i = 1
while True:
    result = 0
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    result = L*(V//P)+min(V % P, L)
    print('Case {}: {}'.format(i, result))
    i += 1
