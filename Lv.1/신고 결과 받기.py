def solution(id_list, report, k):
    mail_dic = {i: 0 for i in id_list}
    reported_dic = {i: 0 for i in id_list}
    for case in set(report):
        reporter, reported = case.split()
        reported_dic[reported] += 1
        if reported_dic[reported] >= k:
            mail_dic[reporter] += 1
    return list(mail_dic.values())