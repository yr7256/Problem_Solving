from collections import defaultdict
T = int(input())
for _ in range(T):
    N = int(input())
    roots = defaultdict(list)
    for _ in range(N-1):
        parent, child = map(int, input().split())
        roots[child] = parent
    a, b = map(int, input().split())
    a_roots, b_roots = [], []
    while a:
        a_roots.append(a)
        a = roots[a]
    while b:
        b_roots.append(b)
        if b in a_roots:
            break
        b = roots[b]
    # print(a_roots, b_roots)
    print(b)