while True:
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break
    else:
        if sum(nums)-max(nums) <= max(nums):
            print('Invalid')
        elif len(set(nums)) == 1:
            print('Equilateral')
        elif len(set(nums)) == 2:
            print('Isosceles')
        else:
            print('Scalene')
