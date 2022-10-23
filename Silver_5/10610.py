N = list(input())
N.sort(reverse=True)
sum = 0
for i in N:
    sum += int(i)
if sum % 3 == 0 and '0' in N:
    print(''.join(N))
else:
    print(-1)
