from itertools import product
colors=set()
for _ in range(2):
    temp = input().split()
    for i in temp:
        colors.add(i)
colors = list(sorted(colors))
for i in product(colors,colors):
    print(*i)