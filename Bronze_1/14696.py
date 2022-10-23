N = int(input())
for i in range(N):
    A = list(map(int, input().split()))[1:]
    B = list(map(int, input().split()))[1:]
    for i in range(4, 0, -1):
        if A.count(i) > B.count(i):
            print('A')
            break
        elif B.count(i) > A.count(i):
            print('B')
            break
    else:
        print('D')
    # dic_A = {4: 0, 3: 0, 2: 0, 1: 0}
    # dic_B = {4: 0, 3: 0, 2: 0, 1: 0}
    # score_A = ''
    # score_B = ''
    # for i in list(map(int, input().split()))[1:]:
    #     dic_A[i] += 1
    # for i in list(map(int, input().split()))[1:]:
    #     dic_B[i] += 1
    # for i in dic_A.values():
    #     score_A += str(i)
    # for i in dic_B.values():
    #     score_B += str(i)
    # score_A = int(score_A)
    # score_B = int(score_B)
    # if score_A > score_B:
    #     print('A')
    # elif score_B > score_A:
    #     print('B')
    # else:
    #     print('D')
