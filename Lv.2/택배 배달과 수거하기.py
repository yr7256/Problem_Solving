from math import ceil


def solution(cap, n, deliveries, pickups):
    answer = 0
    d, p = 0, 0
    for i in range(n-1, -1, -1):
        d += deliveries[i]
        p += pickups[i]
        if d > 0 or p > 0:
            temp = ceil(max(d, p) / cap)
            d -= temp*cap
            p -= temp*cap
            answer += (i+1)*2*temp
    return answer