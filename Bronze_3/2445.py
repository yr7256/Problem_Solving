N = int(input())
for i in range(N):
    print('*'*(i+1)+' '*(2*(N-i-1))+'*'*(i+1))
for j in range(N-1, 0, -1):
    print('*'*j+' '*(2*(N-j))+'*'*j)
