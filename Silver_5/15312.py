A = input()
B = input()
lst = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1,
       2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
nums = []
for i in range(len(A)):
    nums.append(lst[ord(A[i])-65])
    nums.append(lst[ord(B[i])-65])
n = len(nums)
while n != 2:
    temp = []
    for i in range(n-1):
        temp.append((nums[i]+nums[i+1]) % 10)
    n -= 1
    nums = temp
print(''.join(map(str, nums)))
