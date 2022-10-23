b = list(map(int, input().split()))
c = 0
for i in b:
    c += i*i

print(c % 10)
