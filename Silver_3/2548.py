N = int(input())
lst = list(map(int, input().split()))
print(sorted(lst)[(N-1)//2])
