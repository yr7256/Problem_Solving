a = list(map(int, input().split()))
b = list(map(int, input().split()))
A, B = 0, 0
flag = False
for i in range(9):
    A += a[i]
    if A > B:
        flag = True
    B += b[i]
if A < B and flag:
    print('Yes')
else:
    print('No')