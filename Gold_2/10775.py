import sys
input = sys.stdin.readline


def find_root(x):
    if x != airports[x]:  # 루트 찾아야 하는 경우 (그냥 자기가 루트면 찾을 필요x)
        airports[x] = find_root(airports[x])  # 계속 들어가자
    return airports[x]


g = int(input())
p = int(input())
airplanes = [int(input()) for _ in range(p)]
airports = [i for i in range(g+1)]
ans = 0
for airplane in airplanes:
    root = find_root(airplane)
    if root == 0:
        break
    airports[find_root(root)] = find_root(root-1)
    ans += 1
print(ans)


'''
게이트는 1에서 G까지의 번호

'''