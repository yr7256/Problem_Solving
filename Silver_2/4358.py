import sys
input = sys.stdin.readline
trees = {}
N = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
    N += 1
sorted_trees = sorted(trees.keys())
for i in sorted_trees:
    print(f'{i} {trees[i]/N*100:.4f}')
