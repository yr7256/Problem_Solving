N, M = map(int, input().split())
lst = [input() for _ in range(N)]
res = ''
count = 0
for j in range(M):
    A, G, T, C = 0, 0, 0, 0
    for i in range(N):
        if lst[i][j] == 'A':
            A += 1
        elif lst[i][j] == 'C':
            C += 1
        elif lst[i][j] == 'G':
            G += 1
        else:
            T += 1
    if max(A, G, T, C) == A:
        res += 'A'
        count += G+T+C
    elif max(A, G, T, C) == C:
        res += 'C'
        count += A+T+G
    elif max(A, G, T, C) == G:
        res += 'G'
        count += A+T+C
    else:
        res += 'T'
        count += A+C+G

print(res)
print(count)

# N, M = map(int, input().split())
# lst = list(map(list, zip(*[input() for _ in range(N)])))
# res = ''
# count = 0
# for i in range(M):
#     acgt = [0]*4
#     for j in range(N):
#         if lst[i][j] == 'A':
#             acgt[0] += 1
#         elif lst[i][j] == 'C':
#             acgt[1] += 1
#         elif lst[i][j] == 'G':
#             acgt[2] += 1
#         else:
#             acgt[3] += 1
#     if max(acgt) == acgt[0]:
#         res += 'A'
#         count += acgt[1]+acgt[2]+acgt[3]
#     elif max(acgt) == acgt[1]:
#         res += 'C'
#         count += acgt[0]+acgt[2]+acgt[3]
#     elif max(acgt) == acgt[2]:
#         res += 'G'
#         count += acgt[1]+acgt[0]+acgt[3]
#     else:
#         res += 'T'
#         count += acgt[1]+acgt[2]+acgt[0]
# print(res)
# print(count)

# N, M = map(int, input().split())
# lst = list(map(list, zip(*[input() for _ in range(N)])))
# res = ''
# count = 0
# dic_lst = [{'A': 0, 'C': 0, 'G': 0, 'T': 0} for _ in range(M)]
# ans = ''
# count = 0
# for i in range(M):
#     for j in lst[i]:
#         dic_lst[i][j] += 1
# for i in range(M):
#     if dic_lst[i]['A'] == max(dic_lst[i].values()):
#         ans += 'A'
#         count += sum(dic_lst[i].values())-dic_lst[i]['A']
#     elif dic_lst[i]['C'] == max(dic_lst[i].values()):
#         ans += 'C'
#         count += sum(dic_lst[i].values())-dic_lst[i]['C']
#     elif dic_lst[i]['G'] == max(dic_lst[i].values()):
#         ans += 'G'
#         count += sum(dic_lst[i].values())-dic_lst[i]['G']
#     else:
#         ans += 'T'
#         count += sum(dic_lst[i].values())-dic_lst[i]['T']
# print(ans)
# print(count)
