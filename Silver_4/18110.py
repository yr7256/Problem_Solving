def roundTraditional(val):
    return round(val+10**(-len(str(val))-1))


n = int(input())
if n:
    nums = [int(input()) for _ in range(n)]
    nums.sort()
    target = roundTraditional(n*0.15)
    print(roundTraditional(
        sum(nums[target:-target] if target else nums)/(n-2*target)))
else:
    print(0)
