for i in range(3):
    count = 0
    A = list(map(int, input().split()))
    for j in A:
        if j == 1:
            count += 1
    if count == 0:
        print('D')
    elif count == 1:
        print('C')
    elif count == 2:
        print('B')
    elif count == 3:
        print('A')
    else:
        print('E')
