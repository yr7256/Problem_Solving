N, C = map(int, input().split())
dic = {}
for i in map(int, input().split()):
    try:
        dic[i] += 1
    except:
        dic[i] = 1
sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
for i in sorted_dic:
    print(*[i[0]]*i[1], end=' ')
