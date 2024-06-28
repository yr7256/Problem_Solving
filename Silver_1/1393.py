from math import gcd, dist
x0, y0 = map(int, input().split())
x1, y1, dx, dy = map(int, input().split())
dx, dy = dx//gcd(dx, dy), dy//gcd(dx, dy)
while dist([x1, y1], [x0, y0]) > dist([x1+dx, y1+dy], [x0, y0]):
    x1 += dx
    y1 += dy
print(x1, y1)
