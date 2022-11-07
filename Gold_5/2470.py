N = int(input())
lst = list(map(int, input().split()))
lst.sort()
start, end = 0, N-1
ans = 9876543210
s, e = 0, 0
while start < end:
    temp = lst[start] + lst[end]
    if abs(temp) < ans:
        ans = abs(temp)
        s = start
        e = end
    if temp > 0:
        end -=1
    if temp < 0:
        start += 1
    if temp == 0:
        break
print(lst[s], lst[e])

