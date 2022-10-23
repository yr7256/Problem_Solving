import sys


def fac(n):
    if n <= 1:
        return 1
    return n * fac(n-1)


input = sys.stdin.readline
N = int(input())
count = 0
for i in str(fac(N))[::-1]:
    if i != '0':
        break
    count += 1
print(count)
