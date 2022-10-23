'''
일단 a부터 z까지 딕셔너리 하나 만들어보자 (index 기록하는 용도)
그 다음 최대 최소 갱신해줄 수 하나 만들기
최대값이 갱신 안되고 초기값 그대로면 -1 출력해주자.
딕셔너리에 a부터 z까지 일단 index 기록해보자.
그러면 이 딕셔너리의 values()는 인덱스의 리스트들의 모임일 것.
그리고 이 문자열안에 K개가 들어가야 하니까 K-1개의 간격으로 움직일 것이다.
(아래에 예시)

'''
T = int(input())
for i in range(T):
    alpha_dic = dict()
    for j in range(97, 123):
        alpha_dic[chr(j)] = []
    W = input()
    K = int(input())
    min_num, max_num = len(W), -1
    for index, value in enumerate(W):
        alpha_dic[value].append(index)
    for alpha in alpha_dic.values():
        for i in range(len(alpha)-K+1):
            min_num = min(min_num, alpha[i+K-1]-alpha[i]+1)
            max_num = max(max_num, alpha[i+K-1]-alpha[i]+1)
    print(alpha_dic)
    if max_num == -1:
        print(-1)
    else:
        print(min_num, max_num)

'''
1
superaquatornado
2
{'a': [5, 8, 13], 'b': [], 'c': [], 'd': [14], 'e': [3], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 'n': [12], 'o': [10, 15], 'p': [2], 'q': [6], 'r': [4, 11], 's': [0], 't': [9], 'u': [1, 7], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
a 포함한 문자열 만들려면 index가 5~8 혹은 8~13에서 움직여야함.
그리고 이 문자열의 길이는 alpha[i+K-1]-alpha[i]+1 일 것이다.
이 숫자를 계속 갱신시키면서 나아가보자.
range index error 조심하자!
i+K-1에서 에러가 뜨면 안되니까 i의 range는 (len(alpha)-K+1) 일 것이다.
'''