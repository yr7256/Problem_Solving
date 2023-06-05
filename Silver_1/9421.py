def check(num):
    num = list(str(num))
    ans = 0
    for i in num:
        ans += int(i)**2
    return ans


n = int(input())
prime = [False, False]+[True]*(n)
plist = []
for i in range(2, n+1):
    if prime[i]:
        plist.append(i)
        for j in range(2*i, n+1, i):
            prime[j] = False
for j in range(2, n+1):
    if prime[j]:
        temp = set()
        s = j
        while True:
            num = check(s)
            if num in temp:
                if num == 1:
                    print(j)
                break
            temp.add(num)
            s = num
