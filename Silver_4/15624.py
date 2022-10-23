n = int(input())
a, b = 0, 1
num = 1000000007
for i in range(n):
    a, b = (a+b) % num, a % num
print(a)
