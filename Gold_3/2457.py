N = int(input())
date = []
for _ in range(N):
    l_s, l_e, r_s, r_e = map(int, input().split())
    if 100*r_s+r_e < 301 or 100*l_s+l_e > 1130:
        continue
    date.append([100*l_s+l_e, 100*r_s+r_e])
date.sort()
current = [100, 101]
idx = 0
for i in range(N):
    if date[i][0] <= 301:
        if date[i][1] > current[1]:
            current = date[i]
            idx = i
count = 1
while current[1] <= 1130:
    next = [100, 101]
    for i in range(idx, N):
        if current[0] < date[i][0] <= current[1] < date[i][1]:
            if date[i][1] > next[1]:
                next = date[i]
                idx = i
    if next[0] == 100:
        print(0)
        exit()
    current = next
    count += 1
print(count)

'''
[[215, 323], [228, 425], [412, 605], [502, 531],
 [603, 615], [615, 903], [615, 927], [714, 901],
 [914, 1224], [1005, 1231]]
첫 지점 찾기! (피는거, 지는거)
그 다음 인덱스부터 확인하면 되지 않을까?
인덱스 확인해서 첫 지점 지는거보다 다음 지점 피는게 더 앞이면 
그 지점으로 다시 갱신시켜주면 되잖아.
근데 여기서 0은 어떻게 출력시키지..? (고민해보기)
'''
