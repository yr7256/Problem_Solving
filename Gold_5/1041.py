N = int(input())
arr = list(map(int, input().split()))
a, b, c = 5*N**2-16*N+12, 8*N-12, 4
if N == 1:
    print(sum(sorted(arr)[:5]))
else:
    temp = [min(arr[0], arr[5]), min(arr[1], arr[4]), min(arr[2], arr[3])]
    temp.sort()
    temp_a, temp_b, temp_c = temp[0], temp[0]+temp[1], temp[0]+temp[1]+temp[2]
    print(temp_a*a+temp_b*b+temp_c*c)
