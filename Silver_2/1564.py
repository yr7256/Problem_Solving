N = int(input())
a = 4032
for i in range(9, N+1):
    a *= i
    while True:
        if str(a)[-1] == '0':
            a //= 10
        else:
            break
    a %= 10**24
print(str(a)[-5:])
