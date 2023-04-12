K, N = map(int, input().split())
nums = sorted([input() for _ in range(K)])
nums.sort(key=lambda x: int(x))
max_num = nums[-1]
while len(nums) != N:
    nums.append(max_num)
nums.sort(key=lambda x: x*10, reverse=True)
print(''.join(nums))
