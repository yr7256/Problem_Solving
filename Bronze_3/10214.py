T = int(input())
Ycount, Kcount = 0, 0
for _ in range(T):
    for i in range(9):
        Y, K = map(int, input().split())
        Ycount += Y
        Kcount += K
    if Ycount > Kcount:
        print('Yonsei')
    elif Ycount < Kcount:
        print('Korea')
    else:
        print('Draw')
