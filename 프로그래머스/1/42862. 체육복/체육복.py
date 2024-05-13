def solution(n, lost, reserve):
    losts = list(set(lost) - set(reserve))
    losts.sort()
    reserves = set(reserve) - set(lost)
    answer = n - len(losts)
    for l in losts:
        if l - 1 in reserves:
            answer += 1
            reserves.remove(l - 1)
            continue
        if l + 1 in reserves:
            answer += 1
            reserves.remove(l + 1)
            continue
            
    return answer
            