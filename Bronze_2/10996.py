N = int(input())
a = N//2
b = N-a
for i in range(N):
    print('* '*b)
    print(' *'*a)
