lst = []
for i in range(1,13):
    lst.append('w'*i+'o'*i+'l'*i+'f'*i)
S = input()
flag = 1
idx = 0
while idx < len(S):
    flag1 = False
    for wolf in lst:
        if S[idx:idx+len(wolf)] == wolf:
            idx += len(wolf)
            flag1 = True
            break
    if not flag1:
        print(0)
        exit(0)
print(1)
