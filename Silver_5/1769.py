def conv(s, count):
    if len(s) > 1:
        count += 1
        n = 0
        for i in s:
            n += int(i)
        conv(str(n), count)
    else:
        if int(s) % 3 == 0:
            print(count)
            print('YES')
        else:
            print(count)
            print('NO')


X = input()
count = 0
conv(X, count)
