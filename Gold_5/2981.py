from math import gcd
N = int(input())
n = sorted([int(input()) for i in range(N)])
num = []
div = set()
for i in range(N-1, 0, -1):
    num.append(n[i]-n[i-1])
g = num[0]
for i in range(1, len(num)):
    g = gcd(g, num[i])
for i in range(2, int(g**0.5)+1):
    if g % i == 0:
        div.add(i)
        div.add(g//i)
div.add(g)
print(*sorted(list(div)))
