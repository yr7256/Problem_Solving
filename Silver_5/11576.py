A, B = map(int, input().split())
m = int(input())
alist = list(map(int, input().split()))
num = 0
for i in range(m):
    num += alist[i]*(A**(m-i-1))
blist = []
while num != 0:
    blist.append(num % B)
    num //= B
print(*blist[::-1])
