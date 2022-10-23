'''
일단 SWEA때 썼던 코드를 그대로 가져왔습니다..
앞에 풀었던 것과 마찬가지로 이진 탐색이니까 start end 만들고 탐색하는 방법.
다만 end는 가장 오래 걸리는 시간 max(time)*M
중간값에서 심사소요시간을 나눈 것보다 총 인원수가 많다면
시간이 더 오래 걸려야 한다.
반대면 시간이 더 짧게 걸려야 한다.
'''
N, M = map(int, input().split())
time = [int(input()) for _ in range(N)]
left, right = 1, max(time)*M
while left <= right:
    mid = (left+right)//2
    temp = 0
    for ti in time:
        temp += mid//ti
    if temp < M:
        left = mid+1
    else:
        right = mid-1
print(left)