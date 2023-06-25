N, M = map(int, input().split())
nums = list(map(int, input().split()))
temp = 0
arr = [0]*M
for i in range(N):
    temp += nums[i]
    arr[temp%M] += 1
ans = arr[0]
for i in range(M):
    ans += arr[i]*(arr[i]-1)//2
print(ans)


'''
5 3 
1 2 3 1 2

1 3 6 7 9
  2 5 6 8
    3 4 6
      1 3
        2

1 0 0 1 0

나머지가 같은 애들을 빼주면 나머지가 0이겠네.
(3 6 9) (1 7)

3, 6, 9
17
36, 39, 69 

3C2

'''