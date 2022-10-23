odd = []
for i in range(7):
    n = int(input())
    if n % 2 != 0:
        odd.append(n)
if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)
