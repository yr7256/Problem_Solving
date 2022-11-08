r1, c1, r2, c2 = map(int, input().split())
arr = [[0]*(c2-c1+1) for _ in range(r2-c1+1)]
print(arr)