T = int(input())
for i in range(T):
    n, s = input().split()
    print(s[:int(n)-1], s[int(n):], sep='')
