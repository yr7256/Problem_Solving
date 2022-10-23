N = int(input())
a = []
for _ in range(N):
    a.append(input())
a = list(set(a))
a.sort()
a.sort(key=len)
for i in a:
    print(i)
