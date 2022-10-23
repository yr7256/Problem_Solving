K = int(input())
for i in range(K):
    c = list(map(int, input().split()))
    del c[0]
    c.sort()
    gap = []
    print('Class', i+1)
    for i in range(1, len(c)):
        gap.append(c[i]-c[i-1])
    print(f'Max {max(c)}, Min {min(c)}, Largest gap {max(gap)}')
