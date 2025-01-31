'''
젤 큰 원소 찾아서 구하는 아이디어로 접근해보자.
arr_n arr_m 공통 원소 -> 그 중 가장 큰 원소 찾고 index 찾아서 접근해보는 형식 
'''
N = int(input())
arr_n = list(map(int, input().split()))
M = int(input())
arr_m = list(map(int, input().split()))
insec = set(arr_n).intersection(set(arr_m))  # 교집합
ans = []
if not insec:
    print(0)
    exit()  # 넣어야 정답
else:
    while insec:
        target = max(insec)
        ans.append(target)
        idx_n, idx_m = arr_n.index(target), arr_m.index(target)
        arr_n, arr_m = arr_n[idx_n+1:], arr_m[idx_m+1:]
        insec = set(arr_n).intersection(set(arr_m))
print(len(ans))
print(*ans)
