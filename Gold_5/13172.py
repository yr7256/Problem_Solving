import sys
from math import gcd
input = sys.stdin.readline
X = 1000000007
num = 0


def square(a, exp):
    if exp == 1:
        return a
    if exp % 2 == 0:
        half = square(a, exp//2)
        return half*half % X
    else:
        return a*square(a, exp-1) % X


def getnum(n, s):
    return s*square(n, X-2) % X


M = int(input())
for i in range(M):
    n, s = map(int, input().split())
    ns = gcd(n, s)
    n //= ns
    s //= ns
    num += getnum(n, s)
    num %= X
print(num)
