'''
이분 탐색이라고 했으니, start end 사용해서 풀어보자.
일단 검사를 하려면 정렬을 해야 중간을 찾을 수 있다.
i번을 검사한다고 i번 다음부터 끝까지 검색해야한다.
그러니까 index로 따지자면 i+1에서 N-1까지
검색하면서 중간값*0.9보다 크면 표절이고 작으면 아니다.
이분탐색 이용해서 전자라면, start를 중간값으로 잡고 다시 검색하기
(표절 중에 가장 큰 값 찾아야 하니까)
후자라면 end를 중간값으로 잡고 다시 검색하기
이렇게 가장 큰 값 찾고 그 값이 temp라면
temp-i가 0보다 커야 ans에 더해줄 수 있다. (i번째에서 몇번 검사했는지)
'''
N = int(input())
lst = sorted(list(map(int, input().split())))
ans = 0
for i in range(N-1):
    start, end = i+1, N-1
    temp = 0
    while start <= end:
        mid = (start+end)//2
        if lst[i] >= 0.9*lst[mid]:
            start = mid+1
            temp = mid
        else:
            end = mid-1
    if temp-i > 0:
        ans += temp-i
print(ans)