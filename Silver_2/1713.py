N = int(input())
M = int(input())
lst = list(map(int, input().split()))
dic = dict()
count = 0
for num in lst:
    if num in dic:  # 있을 때
        dic[num][0] += 1
    else:  # 없을 때
        if len(dic) >= N and not num in dic:  # dic 길이가 N보다 크거나 같고 이 수가 dict형에 없을 때
            dic.pop(min(dic, key=lambda x: dic[x]))
        dic[num] = [1, count]
        count += 1
print(*sorted(dic))
'''
dic=[추천수,게시된 순서]
'''
# dict형 그냥 정렬하면 key로, value로 정렬하려면 value로

# dic = {1: [3, 2], 2: [1, 2], 3: [1, 3], 4: [2, 5], 5: [3, 1], 6: [4, 3]}
# print(min(dic, key=lambda x: dic[x]))
# print(min(dic.values()))

# 2 1 4 3 5 6 2 7 2
# {1:[1,1],4:[1,2]}
