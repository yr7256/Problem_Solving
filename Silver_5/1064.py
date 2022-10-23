xa, ya, xb, yb, xc, yc = map(int, input().split())
if (xa-xb)*(ya-yc) == (xa-xc)*(ya-yb):
    print(-1.0)
    exit(0)
ab = ((xa-xb)**2+(ya-yb)**2)**0.5
bc = ((xc-xb)**2+(yc-yb)**2)**0.5
ca = ((xa-xc)**2+(ya-yc)**2)**0.5
dist = [ab, bc, ca]
print((max(dist)-min(dist))*2)
