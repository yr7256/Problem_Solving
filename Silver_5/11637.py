T = int(input())
for _ in range(T):
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    majority = sum(lst)//2
    most = max(lst)
    if lst.count(most) == 1:
        if majority < most:
            print('majority winner', lst.index(most)+1)
        else:
            print('minority winner', lst.index(most)+1)
    else:
        print('no winner')