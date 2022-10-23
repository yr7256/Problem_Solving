N = int(input())
A = list(map(int, input().split()))
p_n = 0
for i in A:
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                p_n += 1
            break
print(p_n)
