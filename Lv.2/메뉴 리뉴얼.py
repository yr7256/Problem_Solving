from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    for i in course:
        ans = Counter()
        for order in orders:
            order= sorted(list(order))
            ans += Counter(combinations(order, i))
        answer += [''.join(key) for key, value in ans.most_common()
                   if value == ans.most_common()[0][1] and value > 1]
        answer.sort()
    return answer