def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)


C = int(input())
for _ in range(C):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:])/arr[0]
    count = 0
    for i in arr[1:]:
        if i > avg:
            count += 1
    ans = count/arr[0]*100
    print(f'{roundTraditional(ans,3):.3f}%')
