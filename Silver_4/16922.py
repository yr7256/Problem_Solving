from itertools import combinations_with_replacement
sum_lst = []
N = int(input())
lst = [1, 5, 10, 50]
for c in combinations_with_replacement(range(4), N):
    num = 0
    for i in c:
        num += lst[i]
    sum_lst.append(num)
print(len(set(sum_lst)))
