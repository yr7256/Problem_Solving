from itertools import combinations
from copy import deepcopy


def dist(a, b):                             # 사이거리
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def forward_enemy():    # 적 전진 (인덱스 초과하면 없애기)
    # for x in enemy:   # 리스트 안쓸거니까 폐기하자
    #     x[0] += 1
    #     if x[0] >= N:
    #         enemy.remove(x)
    # return
    return set([(x+1, y) for x, y in enemy if x+1 < N])


def in_range(positions):     # 사격 가능한 좌표 저장하기
    shoot = []
    for position in positions:
        temp = []
        for i in range(N):
            for j in range(M):
                d = dist(position, empty_map[i][j])
                if d <= D:
                    temp.append((i, j, d))      # 거리 계산해서 좌표 넣고 그 좌표 다시
        shoot.append(temp)
    return shoot


def _enemy(possible):   # 먼저 때려야 될 사람 정하기 일단 거리 젤 가까운 애면서, 왼쪽에 있는 친구로 (그냥 x,y만 받으니까 안되더라)
    possible.sort(key=lambda x: (x[2], x[1]))
    for x, y, d in possible:
        if (x, y) in enemy:
            return (x, y)
    return


N, M, D = map(int, input().split())     # D : 사정거리
original_map = [list(map(int, input().split()))
                for _ in range(N)]  # 원래 맵 (이걸로 적 어딨는지 찾을거임)
empty_map = [[0]*M for _ in range(N)]       # 비어있는 맵 (이걸로 사격 가능한 좌표 찾을거임)
for i in range(N):
    for j in range(M):
        empty_map[i][j] = (i, j)
archer = [(N, i) for i in range(M)]         # 궁수들 위치는 가장 밑으로 설정하기
enemy = set()
for i in range(N):
    for j in range(M):
        if original_map[i][j]:
            enemy.add((i, j))
combi = list(combinations(archer, 3))       # 궁수가 어떤 위치의 조합을 가질 수 있을지 알아야 하지.
ans = 0
for pos in combi:   # 조합중에서 하나 뽑아.
    killable = in_range(pos)    # 그 포지션에서 죽일수있는 위치 찾아.
    # print(killable)
    count = 0   # 카운트할거.
    copy_enemy = deepcopy(enemy)    # 적 리스트는 계속 유지해야함.
    while enemy:  # 적 살아있는 동안에
        kill_temp = set()   # 각각의 궁수 한명이 얼마나 죽일수 있을까. (어차피 나중에 밑에서 계속 중복 지울거면 여기서 set으로 해버리기.)
        for p in killable:  # 저장해보자.
            # print(p)
            kill = _enemy(p)    # 주어진 리스트에서 가장 가까우면서 왼쪽인 애 골라서 죽이자.
            if kill:
                kill_temp.add(kill)
            # print(kill)
        count += len(kill_temp)         # 더하는건 리스트랑 똑같은데
        enemy -= kill_temp              # 빼는게 set이 너무 사기다
        enemy = forward_enemy()
    enemy = copy_enemy              # 경우의 수 다 돌았으면 초기화하고 다시 돌리기
    ans = max(ans, count)
print(ans)
