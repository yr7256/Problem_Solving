import sys
import itertools
input = sys.stdin.readline
L, C = map(int, input().split())
str_list = list(map(str, input().split()))
str_list = sorted(str_list)
pw = itertools.combinations(str_list, L)
vowels = ['a', 'e', 'i', 'o', 'u']
for i in pw:
    c = 0
    v = 0
    for j in range(L):
        if i[j] in vowels:
            v += 1
        else:
            c += 1
    if v >= 1 and c >= 2:
        print(''.join(i))
