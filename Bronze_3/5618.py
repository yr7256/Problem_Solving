from math import gcd
n = int(input())
num = gcd(*map(int, input().split()))
s = set()
for i in range(1, int(num**0.5)+1):
    if num % i == 0:
        s.update([i, num//i])
for i in sorted(s):
    print(i)
