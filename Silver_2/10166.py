d1, d2 = map(int, input().split())
nums = [i for i in range(2001)]
ans = 0
for i in range(1, d2+1):
    flag = True
    for j in range(i*2, d2+1, i):
        if flag and d1 <= j and i < d1:
            ans += nums[i]
            flag = False
        nums[j] -= nums[i]
print(sum(nums[d1:d2+1])+ans)

# d1, d2 = map(int, input().split())
# A = set()
# for i in range(d1, d2+1):
#     for j in range(i+1):
#         A.add(j/i)
# print(len(A)-1)
