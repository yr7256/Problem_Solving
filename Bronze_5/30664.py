while True:
    N = int(input())
    if not N:
        break
    if N % 42:
        print('TENTE NOVAMENTE')
    else:
        print('PREMIADO')
