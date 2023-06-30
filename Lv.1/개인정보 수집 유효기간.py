def solution(today, terms, privacies):
    answer = []
    y, m, d = map(int, today.split('.'))
    basis = y*12*28 + m*28 + d
    terms_dic = dict()
    for term in terms:
        term = term.split()
        terms_dic[term[0]] = int(term[1])*28
    for i, privacy in enumerate(privacies):
        temp, term = privacy.split()
        y2, m2, d2 = map(int, temp.split('.'))
        target = y2*12*28 + m2*28 + d2 + terms_dic[term]
        if target <= basis:
            answer.append(i+1)
    return answer