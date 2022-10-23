N = int(input())
dic = {}
ans = ''
for i in range(97, 123):
    dic[chr(i)] = 0
for i in range(N):
    s = input()
    dic[s[0]] += 1
for i in dic:
    if dic[i] >= 5:
        ans += i
if ans:
    print(ans)
else:
    print('PREDAJA')
