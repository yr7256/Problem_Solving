N = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 10**13
result = []
for s in range(N-2):
    m, e = s+1, N-1
    while m < e:
        temp = lst[s]+lst[m]+lst[e]
        if abs(temp) < ans:  # 갱신
            ans = abs(temp)
            result = [lst[s], lst[m], lst[e]]
        if temp < 0:
            m += 1
        elif temp > 0:
            e -= 1
        else:
            print(*result)
            exit(0)
print(*result)

