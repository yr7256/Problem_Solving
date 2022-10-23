N = int(input())
nums = [False, False]+[True]*(N-1)
plist = []
for i in range(2, N+1):
    if nums[i]:
        plist.append(i)
        for j in range(2*i, N+1, i):
            nums[j] = False

# def Prime(N):
#     if N == 1:
#         return False
#     else:
#         for j in range(2, int(N**0.5)+1):
#             if i % j == 0:
#                 return False
#         return True


# plist = []
# for i in range(2, N+1):
#     if Prime(i):
#         plist.append(i)

left, right = 0, 0
psum = 0
answer = 0
sum_length = len(plist)
while True:
    if psum >= N:
        psum -= plist[left]
        left += 1
    else:
        if right == sum_length:
            break
        psum += plist[right]
        right += 1
    if psum == N:
        answer += 1
print(answer)
