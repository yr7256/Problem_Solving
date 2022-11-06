A, B = map(int, input().split())
C = int(input())
if A+B-2*C >= 0:
    print(A+B-2*C)
else:
    print(A+B)
