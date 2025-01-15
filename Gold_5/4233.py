def isprime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if not x % i:
                return False
        return True


def test(x, p):  # x: 밑 , p : 소수판정
    ans = 1
    num = x
    exponent = p
    while exponent:
        if exponent % 2:
            ans = (ans * num) % p
        num = (num * num) % p
        exponent //= 2
    return ans


while True:
    p, a = map(int, input().split())
    if p == 0 and a == 0:
        break
    if not isprime(p) and test(a, p) == a:
        print('yes')
    else:
        print('no')
