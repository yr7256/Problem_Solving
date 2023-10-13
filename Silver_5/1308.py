from datetime import date
y, m, d = map(int, input().split())
yy, mm, dd = map(int, input().split())
if y+1000 < yy:
    print('gg')
elif y+1000 == yy and (m, d) <= (mm, dd):
    print('gg')
else:
    print(f'D{date(y,m,d).toordinal()-date(yy,mm,dd).toordinal()}')
