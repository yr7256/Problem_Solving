d = ['N', 'E', 'S', 'W']
ans = 0
for i in range(10):
    c = int(input())
    if c == 1:
        ans += 1
    elif c == 2:
        ans += 2
    else:
        ans += 3
print(d[ans % 4])
