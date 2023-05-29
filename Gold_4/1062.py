import sys
from itertools import combinations


def bit(word):
    res = 0
    for w in word:
        res |= 1 << available_bin[w]
    return res


input = sys.stdin.readline
N, K = map(int, input().split())
ans = 0
alpha = {'a', 'n', 't', 'i', 'c'}
words = [set(input().strip()[4:-4]) - alpha for _ in range(N)]
available = set(chr(i) for i in range(97, 123)) - alpha
available_bin = {val: num for num, val in enumerate(available)}

if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    words_bin = [bit(word) for word in words]
    for c in combinations([2**i for i in range(21)], K-5):
        temp = 0
        c_sum = sum(c)
        for word_bin in words_bin:
            if word_bin & c_sum == word_bin:
                temp += 1
        ans = max(ans, temp)
    print(ans)
