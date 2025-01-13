import sys


def find_root(x):
    if x != nums[x]:  # 루트 찾아야 하는 경우 (그냥 자기가 루트면 찾을 필요x)
        nums[x] = find_root(nums[x])  # 계속 들어가자
    return nums[x]


input = sys.stdin.readline
N = int(input())
M = int(input())
info = []
nums = [i for i in range(N+1)]
ans = 0
for i in range(M):
    a, b, c = map(int, input().split())
    info.append([a, b, c])
info.sort(key=lambda x: (x[2], x[0]))
for a, b, c in info:
    if find_root(a) != find_root(b):
        s, e = min(find_root(a), find_root(b)), max(find_root(a), find_root(b))
        nums[e] = s
        ans += c
print(ans)
