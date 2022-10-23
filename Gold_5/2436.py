from math import gcd
A, B = map(int, input().split())
C = B//A
lst = []
for i in range(1, int(C**0.5)+1):
    if C % i == 0:
        if gcd(i, C//i) == 1:
            lst.append([i+C//i, i, C//i])
lst.sort()
print(lst[0][1]*A, lst[0][2]*A)
