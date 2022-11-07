import sys  # input이 최대 123457줄이 나올 수 있으므로 필수!!
input = sys.stdin.readline
N, H0 = map(int, input().split())
ans = 0
temp = 0  # 현재 피해 받은 양
for i in range(N):
    t, a, h = map(int, input().split())
    if t == 1:  # 몬스터일 때
        q, r = h // H0, h % H0  # 몫, 나머지 
        if r:  # ex) 내가 7대 때려서 죽으면 몬스터에게는 6대만 맞는다
            temp += a*q
        else:
            temp += a*(q-1)
    else:  # 포션일 때
        H0 += a  
        temp -= h  # 체력 회복
    if temp < 0:  # 0 미만 이라는건 회복량 오버라는 소리 
        temp = 0  # 그러면 0으로 초기화
    ans = max(ans, temp)  # 갱신해줘야 하는 이유 : 체력 아무리 많이 받았어도 마지막쯤에 체력회복 다 해버리면 소용없음. 그러므로 순간순간 갱신이 필요하다
print(ans+1)
