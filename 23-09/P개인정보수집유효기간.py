def destroy(today, term, privacy):
    today_y, today_m, today_d = today.split(".")
    pri_y, pri_m, pri_d = privacy.split(".")
    
    today_y = int(today_y)
    today_m = int(today_m)
    today_d = int(today_d)
    pri_y = int(pri_y)
    pri_m = int(pri_m)
    pri_d = int(pri_d)
    term = int(term)
    
    pri_d -= 1
    if pri_d == 0:
        pri_d = 28
        pri_m -= 1
    pri_m += term
    if pri_m > 12:
        pri_y = pri_y + (pri_m - 1) // 12
        pri_m = (pri_m - 1) % 12 + 1
    
    if pri_y < today_y:
        return True
    elif pri_y == today_y:
        if pri_m < today_m:
            return True
        elif pri_m == today_m:
            if pri_d < today_d:
                return True
            else:
                return False
        else: 
            return False
    else:
        return False
    
    
def solution(today, terms, privacies):
    answer = []
    
    for i in range(len(privacies)):
        for term in terms:
            if privacies[i][-1] == term[0]:
                if destroy(today, term[2:], privacies[i][:10]):
                    answer.append(i + 1)
                    
    return answer