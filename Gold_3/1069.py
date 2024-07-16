# 경우의 수
# 1. 그냥 걷기
# 2. 점프하고 걷기
# 3. 점프로만 가는 방법 -> 각도 바꾸면서 일직선보다 한번 더 뛰는 방법
# 남은 거리가 점프 거리보다 작다면?
# 1. 오버해서 뛰고 나머지 걷기
# 2. 각도 바꾸면서 2번 뛰기 (3번 이상은 비효율적)
# 3. 그냥 걷기
from math import dist
X, Y, D, T = map(int, input().split())
d = dist((X, Y), (0, 0))
if d >= D:
    ans = min(d, T*(d//D)+d % D, T*(d//D+1))
else:
    ans = min(T+(D-d), 2*T, d)
print(ans)
