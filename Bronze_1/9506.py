while True:
    n = int(input())
    if n == -1:
        break
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
    if sum(div) == n:
        print(n, '=', ' + '.join(str(i) for i in div))
    else:
        print(n, 'is NOT perfect.')
