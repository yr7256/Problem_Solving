N = int(input())
C = [int(input()) for i in range(N)]
C.sort(reverse=True)
result = 0
for i in range(2, N, 3):
    result += C[i]
print(sum(C)-result)
