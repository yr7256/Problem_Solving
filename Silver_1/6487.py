N = int(input())
for _ in range(N):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    a, b, c, d = x2-x1, y2-y1, x4-x3, y4-y3
    disc = a*d-b*c
    if disc:
        r = ((x3-x1)*d-(y3-y1)*c)/disc
        print('POINT {:.2f} {:.2f}'.format(x1+a*r, y1+b*r))
    else:
        print('NONE' if (x3-x1)*b-(y3-y1)*a else 'LINE')
