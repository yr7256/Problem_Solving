a = 1
while True:
    L = int(input())
    if not L:
        break
    N = int(input())
    print('User', a)
    for i in range(N):
        print('{:.5f}'.format(L*int(input())/100000))
    a += 1
