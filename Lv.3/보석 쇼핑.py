from collections import defaultdict             # dict형 편하게 관리하기 위해 defaultdict 사용


def solution(gems):                             #
    answer = [0, len(gems)]                     # 최대보다 큰 구간으로 처음 구간을 정한다.
    start, end = 0, 0                           # 투 포인터 사용
    kind = len(set(gems))                       # 보석의 종류
    gem_dic = defaultdict(int)                  # 구간에서 보석의 종류와 갯수 카운트하는 dict
    gem_dic[gems[start]] = 1                    # 
    while start <= end:                         # 
        if len(gem_dic) == kind:                # 특정 구간에서 보석의 모든 종류가 있는데
            if end-start < answer[1]-answer[0]: # 이 구간이 answer의 길이보다 작다면
                answer = [start+1, end+1]       # 갱신해준다. (index가 1부터 시작하니까 +1 해주기)
            else:                               # 이 구간이 answer의 길이보다 크다면
                gem_dic[gems[start]] -= 1       # 왼쪽 포인터를 이동
                if not gem_dic[gems[start]]:    # 만약 이 요소의 value가 0 이라면 요소를 제거한다.
                    del gem_dic[gems[start]]    # (value가 0이라도 key는 남아있기 때문)
                start += 1                      # 
        else:                                   # 구간에서 아직 보석이 다 모이지 않았다면
            end += 1                            # 오른쪽 포인터를 이동
            if end == len(gems):
                break
            gem_dic[gems[end]] += 1

    return answer