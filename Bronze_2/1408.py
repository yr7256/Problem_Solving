a, b, c = map(int, input().split(':'))
d, e, f = map(int, input().split(':'))
res = (d-a)*3600+(e-b)*60+f-c
if res < 0:
    res += 86400
print(str(res//3600).zfill(2), str((res % 3600) //
      60).zfill(2), str(res % 60).zfill(2), sep=':')
