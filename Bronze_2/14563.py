T = int(input())
for num in map(int, input().split()):
    res = 0
    for i in range(1, num):
        if not num % i:
            res += i
    if res == num:
        print('Perfect')
    elif res > num:
        print('Abundant')
    else:
        print('Deficient')
