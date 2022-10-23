N = input()
n = [0]*10
for i in N:
    if i == '6' or i == '9':
        n[6] += 1
    else:
        n[int(i)] += 1
if n[6] % 2 == 0:
    n[6] = n[6]//2
else:
    n[6] = n[6]//2 + 1
print(max(n))
