T = int(input())
for i in range(T):
    ans = ''
    nums = sorted(list(map(int, input().split())))
    if nums[0]**2+nums[1]**2 == nums[2]**2:
        ans = 'yes'
    else:
        ans = 'no'
    print(f'Scenario #{i+1}:')
    print(ans)
    print()