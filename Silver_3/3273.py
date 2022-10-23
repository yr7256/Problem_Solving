n = int(input())
A = list(map(int, input().split()))
x = int(input())
A.sort()
count = 0
start, end = 0, n-1
while start != end:
    if A[start]+A[end] == x:
        count += 1
        start += 1
    elif A[start]+A[end] > x:
        end -= 1
    else:
        start += 1
print(count)
