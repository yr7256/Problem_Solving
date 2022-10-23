def binary(n):
    start, end = 1, n
    while start <= end:
        mid = (start+end)//2
        if mid ** 2 > n:
            end = mid-1
        elif mid ** 2 < n:
            start = mid+1
        else:
            return mid


N = int(input())
print(binary(N))
