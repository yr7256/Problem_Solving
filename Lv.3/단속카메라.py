def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    current = -30001
    for route in routes:
        if current < route[0]:
            answer += 1
            current = route[1]
    return answer