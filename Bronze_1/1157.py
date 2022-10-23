S = input().upper()
S_list = list(set(S))
n_count = []
for i in S_list:
    w_count = S.count(i)
    n_count.append(w_count)
if n_count.count(max(n_count)) > 1:
    print('?')
else:
    print(S_list[n_count.index(max(n_count))])

# import statistics
# s = input().upper()
# m = statistics.multimode(s)
# if len(m) > 1:
#     print('?')
# else:
#     print(m[0])
