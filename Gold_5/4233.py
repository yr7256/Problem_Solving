def isprime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if not x % i:
                return False
        return True


while True:
    p, a = map(int, input().split())
    if p == 0 and a == 0:
        break
    if not isprime(p):
        print('Yes')
    else:
        print('No')
