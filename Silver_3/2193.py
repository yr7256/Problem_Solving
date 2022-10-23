num = [0, 1, 1]
for i in range(3, 91):
    num.append(num[i-2]+num[i-1])
N = int(input())
print(num[N])
