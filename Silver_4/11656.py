S = list(input())
S_list = []
for i in range(len(S)):
    S_list.append(''.join(S))
    S.remove(S[0])
S_list.sort()
for i in S_list:
    print(i)
