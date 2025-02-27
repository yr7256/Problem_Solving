N = int(input())
arr = list(map(int, input().split()))
prefix_sum = [0]*(N+1)
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1]+arr[i-1]  # i까지 꿀 채취양
ans = 0
for i in range(1, N-1):
    ans = max(ans, prefix_sum[N-1]+prefix_sum[i]-arr[i])
    # 벌통 왼쪽, 벌 오른쪽 고정시키고 한명 이동
    # 이 케이스일 때, 맨 오른쪽 벌은 prefix-sum[N-1]-arr[i], i번째 벌은 prefix_sum[i]
    ans = max(ans, prefix_sum[N]*2-arr[0]-arr[i]-prefix_sum[i+1])
    # 벌통 오른쪽, 벌 왼쪽 고정 시키고 한명 이동
    # 이 케이스일 때, 맨 왼쪽 벌은 prefix_sum[N]-arr[0]-arr[i], i번째 벌은 prefix_sum[N]-prefix_sum[i+1]
    ans = max(ans, prefix_sum[N-1]-arr[0]+arr[i])
    # 벌 왼쪽, 오른쪽 고정 시키고 벌통 이동
    # 이 케이스일 때, 중복은 i번째 꿀통, 그래서 맨 왼쪽과 오른쪽 제외하고 arr[i] 더하기
print(ans)
