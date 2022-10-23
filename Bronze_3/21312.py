import sys
input = sys.stdin.readline
D = list(map(int, input().split()))
odd = []
result = 1
for i in range(3):
    if D[i] % 2 == 1:
        odd.append(D[i])
if odd:
    for i in odd:
        result *= i
else:
    for i in D:
        result *= i
print(result)

# a,b,c=map(int,input().split())
# print(max([(x%2,x) for x in [a,b,c,a*b,b*c,c*a,a*b*c]])[1])
