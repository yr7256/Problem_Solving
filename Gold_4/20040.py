'''
점 n개 주어진다. 0에서 n-1까지 어느 세 점도 일직선 위에 놓이지 않는다.
플레이어는 두 점을 선택해서 연결한다. 이전 선분 다시 긋기 x 교차 o
사이클 완성하면 게임 끝.
* 아이디어
루트 찾기 - 어떻게 찾을건데? 재귀로!
'''
import sys
input = sys.stdin.readline


def find_root(x):
    if x != nums[x]:  # 루트 찾아야 하는 경우 (그냥 자기가 루트면 찾을 필요x)
        nums[x] = find_root(nums[x])  # 계속 들어가자
    return nums[x]


n, m = map(int, input().split())
nums = [i for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if find_root(a) == find_root(b):
        print(i+1)
        break
    s, e = min(find_root(a), find_root(b)), max(find_root(a), find_root(b))
    nums[e] = s
else:
    print(0)
