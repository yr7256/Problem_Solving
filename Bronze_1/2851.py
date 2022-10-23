sum_num = 0
lst = [int(input()) for _ in range(10)]
for i in lst:
    sum_num += i
    if sum_num >= 100:
        if 100-(sum_num-i) < sum_num-100:
            sum_num -= i
        break
print(sum_num)
