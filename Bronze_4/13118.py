p = list(map(int, input().split()))
x, y, r = map(int, input().split())
print(p.index(x)+1 if x in p else 0)
