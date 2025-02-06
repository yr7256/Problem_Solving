def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
p1, p2, p3, p4 = [x1, y1], [x2, y2], [x3, y3], [x4, y4]
mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)
d1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
d2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)
ans = 0
if d1 == 0 and d2 == 0:
    if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
        ans = 1
elif d1 <= 0 and d2 <= 0:
    ans = 1
print(ans)
