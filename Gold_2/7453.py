'''
4000줄 있고 a b c d 경우의 수 계산하면
abcd를 두개씩 묶어서 계산하는게 빠르지 않을까
이진탐색 bisect left right로 시도해보기
'''
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ab = []
cd = []
for i in range(n):
    for j in range(n):
        ab.append(arr[i][0]+arr[j][1])
        cd.append(arr[i][2]+arr[j][3])
ab.sort()
cd.sort()
start, end = 0, n**2-1
ans = 0
while 0 <= start < n**2 and 0 <= end < n**2:
    target = ab[start]+cd[end]
    if target < 0:
        start += 1
    elif target > 0:
        end -= 1
    else:  # 이 시점에서 ab와 cd에서 동읽한 값이 나올 수 있으니까 이진탐색
        abstart, abend = bisect_left(
            ab, ab[start]), bisect_right(ab, ab[start])
        cdstart, cdend = bisect_left(cd, cd[end]), bisect_right(cd, cd[end])
        ans += (abend - abstart)*(cdend-cdstart)
        start = abend
        end = cdstart-1
print(ans)
