from itertools import permutations
N = int(input())
arr = list(input().split())
arr = list(set(arr))
ans = set()
if len(arr) == 1:
    print('1')
    print(max(arr[0]))
    exit()
for combi in permutations(arr, 2):
    ans.add(max(combi[0][0], combi[1][1]))
print(len(ans))
print(*sorted(ans))
