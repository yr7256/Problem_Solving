N = int(input())
dic = {}
for i in range(N):
    s = input()
    l = len(s)
    for j in s:
        if j in dic:
            dic[j] += 10**(l-1)
        else:
            dic[j] = 10**(l-1)
        l -= 1
dic = sorted(dic.values(), reverse=True)
answer = 0
m = 9
for i in dic:
    answer += i*m
    m -= 1
print(answer)
