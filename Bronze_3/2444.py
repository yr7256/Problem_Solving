N = int(input())
for i in range(N):
    print(' '*(N-i-1)+'*'*((2*i)+1))
for j in range(N-1, 0, -1):
    print(' '*(N-j)+'*'*((2*j)-1))
