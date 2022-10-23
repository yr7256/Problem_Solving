while True:
    n = input()
    if n == '0':
        break
    elif n[::-1] == n:
        print('yes')
    else:
        print('no')
