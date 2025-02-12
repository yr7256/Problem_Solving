k = int(input())
nums = list(map(int, input().split()))
max_val = sum(nums)
weights = {0}
for i in nums:
    temp = set()
    for w in weights:
        temp.add(w + i)
        temp.add(abs(w - i))
    weights |= temp
print(max_val-len(weights)+1)
