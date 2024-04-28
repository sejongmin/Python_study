def solution(id_list, report, k):
    answer = {user_id:0 for user_id in id_list}
    report_dict = {user_id:set() for user_id in id_list}
    
    for s in report:
        reporter, user_id = s.split()
        report_dict[user_id].add(reporter)
    
    for value in report_dict.values():
        if len(value) >= k:
            for v in value:
                answer[v] += 1
    
    return list(answer.values())