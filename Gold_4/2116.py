"""
주사위 반대편에 있는 수 저장해줘야한다.
그래야 top bottom 빼고 최대인 수 뽑아낼 수 있다.
그리고 위 주사위 bottom은 아래 주사위 top이랑 같은거니까 저장하면서
top bottom 빼고 최대인 수 다시 temp에 저장해주자.
그 다음 temp랑 max_num 비교해주면서 최대인 수 찾아내기
for j in range(1, N) <- 맨 위는 for i in range(6)로 저장해줄거니까 필요x
"""
opposite = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
N = int(input())
max_num = 0
dice_list = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
for i in range(6):
    top_num = dice_list[0][i]
    bottom_num = dice_list[0][opposite[i]]
    temp = max([x for x in dice_list[0] if not (
        x == top_num or x == bottom_num)])
    for j in range(1, N):
        top_num = bottom_num
        bottom_num = dice_list[j][opposite[dice_list[j].index(top_num)]]
        temp += max([x for x in dice_list[j]
                    if not (x == top_num or x == bottom_num)])
    max_num = max(max_num, temp)
print(max_num)
