lst = []
for i in range(5):
    if 'FBI' in input():
        lst.append(i+1)
if lst:
    print(*lst)
else:
    print('HE GOT AWAY!')