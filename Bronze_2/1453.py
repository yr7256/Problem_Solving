N = int(input())
lst = list(map(int, input().split()))
set_lst = set(lst)
print(len(lst)-len(set_lst))
