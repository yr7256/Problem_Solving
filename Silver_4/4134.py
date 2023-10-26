import sys


def isprime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if not x % i:
                return False
        return True


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    while True:
        if isprime(n):
            print(n)
            break
        else:
            n += 1
