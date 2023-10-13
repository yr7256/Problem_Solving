from itertools import product
N, K = input().split()
arr = list(map(str, input().split()))
l = len(N)
N = int(N)
while True:
    nums = []
    for i in list(product(arr, repeat=l)):
        n = int(''.join(i))
        if n <= N:
            nums.append(n)
    if nums:
        print(max(nums))
        break
    else:
        l -= 1
