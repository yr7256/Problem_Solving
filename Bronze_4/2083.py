while True:
    A, B, C = input().split()
    if int(B) > 17 or int(C) >= 80:
        print(A, 'Senior')
    elif A == '#' and B == '0' and C == '0':
        break
    else:
        print(A, 'Junior')
