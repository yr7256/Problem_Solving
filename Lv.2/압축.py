def solution(msg):
    answer = []
    dic = dict()
    for i in range(65, 91):
        dic[chr(i)] = i-64
    n = 27
    idx = 0
    l = 0
    while True:
        l += 1
        if not dic.get(msg[idx:idx+l]):
            answer.append(dic[msg[idx:idx+l-1]])
            dic[msg[idx:idx+l]] = n
            n += 1
            idx += l-1
            l = 0
        else:
            if idx+l == len(msg):
                answer.append(dic[msg[idx:idx+l]])
                break
    return answer