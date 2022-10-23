S = input()
check = 'UCPC'
i = 0
for s in S:
    if s == check[i]:
        i += 1
    if i == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')
