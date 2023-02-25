n = int(input())
s, e = 0, n
while s <= e:
    m = (s+e)//2
    if m**2 < n:
        s = m+1
    else:
        e = m-1
print(s)
