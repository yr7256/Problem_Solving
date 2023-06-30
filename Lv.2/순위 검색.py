from itertools import combinations
from collections import defaultdict


def solution(info, query):
    answer = []
    infos = defaultdict(list)
    for i in info:
        i = i.split()
        for j in range(5):
            for c in combinations(i[:-1], j):
                infos[''.join(c)].append(int(i[-1]))
    for k in infos.keys():
        infos[k].sort()
    for q in query:
        q = q.replace('and', '').replace('-', '').split()
        target = infos[''.join(q[:-1])]
        s, e = 0, len(target)
        while s < e:
            m = (s+e)//2
            if target[m] < int(q[-1]):
                s = m+1
            else:
                e = m
        answer.append(len(target)-s)
    return answer