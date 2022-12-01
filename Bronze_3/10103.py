n = int(input())
a, b = 100, 100
for i in range(n):
    l, r = map(int, input().split())
    if l < r:
        a -= r
    if l > r:
        b -= l
print(a)
print(b)
