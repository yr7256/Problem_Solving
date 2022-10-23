from collections import deque
N = int(input())
building = [[] for _ in range(N+1)]  # n번째 인덱스에 있는 건물이 어느 건물을 완성하는 데 필요할까?
cost = [0]*(N+1)  # 만드는 데 필요한 시간의 리스트
depth = [0]*(N+1)  # n번째 인덱스의 건물이 어느 정도의 깊이까지 들어갈까
for i in range(1, N+1):
    info = list(map(int, input().split()))[:-1]
    cost[i] = info[0]
    data = info[1:]
    for d in data:
        building[d].append(i)
        depth[i] += 1
# print(building)
# print(depth)
answer = [0]*(N+1)  # 최종적으로 얼마의 시간이 들어갈 지 저장해주는 리스트
queue = deque([])
for i in range(1, N+1):
    if not depth[i]:  # 모든 건물이 depth가 1 이상 일 수는 없다!
        # (무조건 지어지는 건물이 있어야 다른 건물도 지어질 것)
        queue.append(i)  # 그 것들부터 탐색해보자
while queue:
    current = queue.popleft()
    answer[current] += cost[current]  # 탐색해서 더해주자
    for target in building[current]:
        depth[target] -= 1  # 더했으면 일단 깊이 하나 줄이자 (최종적으로는 모두의 깊이가 0이 되게)
        answer[target] = max(answer[target], answer[current])  # 값 갱신해주기
        if not depth[target]:
            queue.append(target) 
for i in answer[1:]:
    print(i)
