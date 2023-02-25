while True:
    N = input()
    if N == '0':
        break
    print(len(N)*4+1+N.count('0')-N.count('1'))
