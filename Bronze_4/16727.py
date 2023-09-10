a, b = map(int, input().split())
c, d = map(int, input().split())
x = a+d
y = b+c
if x == y:
    if b == d:
        print('Penalty')
    elif b > d:
        print('Esteghlal')
    else:
        print('Persepolis')
else:
    print('Persepolis' if x > y else 'Esteghlal')
