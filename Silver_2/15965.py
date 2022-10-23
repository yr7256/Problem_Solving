num = 10**7
p = [1]*num
for i in range(2, int(num**0.5)+1):
    if p[i]:
        for j in range(i*2, num, i):
            p[j] = 0
p_list = [i for i in range(2, num) if p[i]]
K = int(input())
print(p_list[K-1])
