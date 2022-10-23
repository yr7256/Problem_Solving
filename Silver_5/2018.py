N = int(input())
count = 0
for i in range(1, N+1):
    if i*2 <= 2*N-i**2+i and not (2*N-i**2+i) % (2*i):
        count += 1
print(count)
