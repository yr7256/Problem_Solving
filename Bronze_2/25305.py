N, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
print(lst[N-k])