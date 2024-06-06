N = int(input())
S = input()
flag = True
cnt = 0
for i in range(N-1):
    if S[i] != S[i+1] and flag:
        cnt += 1
        flag = False
    else:
        flag = True
print(cnt)
