N = int(input())
num = list(map(int, input().split()))
flag = False
for i in range(N-1, 0, -1):
    if num[i-1] < num[i]:
        for j in range(N-1, 0, -1):
            if num[i-1] < num[j]:
                num[i-1], num[j] = num[j], num[i-1]
                result = num[:i]+sorted(num[i:])
                flag = True
                break
    if flag:
        print(*result)
        break
else:
    print(-1)
