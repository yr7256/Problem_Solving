N = int(input())
lst = list(map(int, input().split()))
y, m = 0, 0
for i in lst:
    y += (i//30+1)*10
    m += (i//60+1)*15
if y < m:
    print('Y', y)
elif y > m:
    print('M', m)
else:
    print('Y M', y)
