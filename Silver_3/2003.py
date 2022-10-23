N, M = map(int, input().split())
A = list(map(int, input().split()))
start, end = 0, 0
count = 0
while start <= end <= N:
    answer = sum(A[start:end])
    if answer == M:
        count += 1
    if answer <= M:
        end += 1
        continue
    elif answer > M and start < end:
        start += 1
        continue
    else:
        start += 1
        end += 1
print(count)
