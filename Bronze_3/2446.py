N = int(input())
for i in range(N, 0, -1):
    print(' '*(N-i)+'*'*((2*i)-1))
for j in range(1, N):
    print(' '*(N-j-1)+'*'*((2*j)+1))
