nums = [int(input()) for _ in range(6)]
A = nums[0]*3+nums[1]*2+nums[2]
B = nums[3]*3+nums[4]*2+nums[5]
if A == B:
    print('T')
else:
    print('A' if A > B else 'B')
