from collections import Counter
dic = Counter(input())
odd = ""
odd_count = 0
for i in dic:
    if dic[i] % 2 == 1:
        odd = i
        odd_count += 1
if odd_count >= 2:
    answer = "I'm Sorry Hansoo"
else:
    sorted_dic = sorted(dic.items())
    half = ''
    for i in range(len(sorted_dic)):
        half += sorted_dic[i][0] * int(sorted_dic[i][1] / 2)
    answer = half + odd + half[::-1]
print(answer)
