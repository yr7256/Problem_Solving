n = int(input())
o, e = 0, 0
for i in map(int, input().split()):
    if i % 2:
        o += 1
    else:
        e += 1
print('Happy' if e>o else 'Sad')
